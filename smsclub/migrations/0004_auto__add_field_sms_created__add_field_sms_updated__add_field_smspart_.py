# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sms.created'
        db.add_column(u'sms_sms', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 17, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Sms.updated'
        db.add_column(u'sms_sms', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 3, 17, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SmsPart.created'
        db.add_column(u'sms_smspart', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 17, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SmsPart.updated'
        db.add_column(u'sms_smspart', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 3, 17, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sms.created'
        db.delete_column(u'sms_sms', 'created')

        # Deleting field 'Sms.updated'
        db.delete_column(u'sms_sms', 'updated')

        # Deleting field 'SmsPart.created'
        db.delete_column(u'sms_smspart', 'created')

        # Deleting field 'SmsPart.updated'
        db.delete_column(u'sms_smspart', 'updated')


    models = {
        u'sms.sms': {
            'Meta': {'object_name': 'Sms'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'result_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'sms.smspart': {
            'Meta': {'object_name': 'SmsPart'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sms.Sms']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NOREPORT'", 'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sms']