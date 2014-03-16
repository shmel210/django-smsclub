# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'SmsPart', fields ['part']
        db.create_unique(u'sms_smspart', ['part'])


    def backwards(self, orm):
        # Removing unique constraint on 'SmsPart', fields ['part']
        db.delete_unique(u'sms_smspart', ['part'])


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
            'part': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sms.Sms']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NOREPORT'", 'max_length': '100'})
        }
    }

    complete_apps = ['sms']