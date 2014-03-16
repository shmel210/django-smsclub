# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sms(models.Model):
    phone = models.CharField(_('phone'), max_length=14)
    result_text = models.CharField(_('result_text'), max_length=255)
    status = models.CharField(_('status'), max_length=100)
    body = models.TextField(_('body'))


class SmsPart(models.Model):
    sms = models.ForeignKey('Sms')
    part = models.CharField(_('part'), max_length=255, unique=True)
    state = models.CharField(_('state'), max_length=100, default='NOREPORT')