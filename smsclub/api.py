from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import loader, Context
from smsclub.models import Sms, SmsPart
import httplib2
import urllib
from xml.dom.minidom import parseString
import logging
logger = logging.getLogger(__name__)
try:
    SMS_USERNAME = settings.SMS_USERNAME
    SMS_PASSWORD = settings.SMS_PASSWORD
except AttributeError:
    raise ImproperlyConfigured('django-sms requires SMS_USERNAME and SMS_PASSWORD to be configured')
SMS_SEND_URL = getattr(settings, 'SMS_SEND_URL', 'http://smpp.smsclub.mobi/hfw_smpp_addon/xmlsendindividual.php ')
SMS_STATUS_URL = getattr(settings, 'SMS_STATUS_URL', 'http://smpp.smsclub.mobi/hfw_smpp_addon/xmlgetsmsstatepost.php ')


def parse_sms_response(response, content, to_text):
    if response.status != 200:
        logger.error(u'cant access to sms gateway. Response status: %s' % (response.status,))
        return {
            'status': 'ERROR',
            'text': 'cant access to sms gateway',
        }
    else:
        content = '<?xml version="1.0" encoding="utf-8"?><response><status>OK</status><text>dsf</text><ids><mess>p0066a46dc</mess></ids></response>'
        dom = parseString(content)
        phones = {}
        sms_sended = []
        for (phone, text) in to_text:
            sms = Sms(phone=phone, result_text=dom.getElementsByTagName('text')[0].childNodes[0].data,
                      status=dom.getElementsByTagName('status')[0].childNodes[0].data, body=text)
            sms.save()
            sms_sended.append(sms)
            for mess in dom.getElementsByTagName('mess'):
                try:
                    if mess.attributes['tel'].value == phone.replace('+', ''):
                        SmsPart(sms=sms, part=mess.childNodes[0].data).save()
                except KeyError:
                    SmsPart(sms=sms, part=mess.childNodes[0].data).save()
        return sms_sended


'''
frm = 'FROM USERNAME'
to_text = (
    ('380994442211', 'some text'),
    ('380992221112', 'another text'),
)
'''
def send(frm, to_text):
    t = loader.get_template('sms/send.xml')
    xml = t.render(Context({
        'username': SMS_USERNAME,
        'password': SMS_PASSWORD,
        'to_text': to_text,
        'from': frm,
    }))
    body = urllib.urlencode({'xmlrequest': unicode(xml).encode('utf-8')})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response, content = httplib2.Http().request(SMS_SEND_URL, headers=headers, method='POST', body=body)
    logger.debug(unicode(xml).encode('utf-8'))
    logger.debug(content)
    return parse_sms_response(response, content, to_text)


def get_status(parts):
    t = loader.get_template('sms/status.xml')
    xml = t.render(Context({
        'username': SMS_USERNAME,
        'password': SMS_PASSWORD,
        'parts': parts,
    }))
    sms_parts = []
    body = urllib.urlencode({'xmlrequest': unicode(xml).encode('utf-8')})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response, content = httplib2.Http().request(SMS_STATUS_URL, headers=headers, method='POST', body=body)
    logger.debug(unicode(xml).encode('utf-8'))
    logger.debug(content)
    if response.status != 200:
        logger.error(u'cant access to sms gateway. Response status: %s' % (response.status,))
        return {
            'status': 'ERROR',
            'text': 'cant access to sms gateway',
        }
    else:
        dom = parseString(content)
        for key, smscid in enumerate(dom.getElementsByTagName('smscid')):
            part = SmsPart.objects.get(part=smscid.childNodes[0].data)
            if part.state != dom.getElementsByTagName('state')[key].childNodes[0].data:
                part.state = dom.getElementsByTagName('state')[key].childNodes[0].data
                part.save()
            sms_parts.append(part)
    return sms_parts
