# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SmsPart.state'
        db.add_column(u'sms_smspart', 'state',
                      self.gf('django.db.models.fields.CharField')(default='NOREPORT', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SmsPart.state'
        db.delete_column(u'sms_smspart', 'state')


    models = {
        u'sms.sms': {
            'Meta': {'object_name': 'Sms'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'result_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sms.smspart': {
            'Meta': {'object_name': 'SmsPart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sms.Sms']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NOREPORT'", 'max_length': '100'})
        }
    }

    complete_apps = ['sms']