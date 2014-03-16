# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sms'
        db.create_table(u'sms_sms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('result_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'sms', ['Sms'])

        # Adding model 'SmsPart'
        db.create_table(u'sms_smspart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sms.Sms'])),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'sms', ['SmsPart'])


    def backwards(self, orm):
        # Deleting model 'Sms'
        db.delete_table(u'sms_sms')

        # Deleting model 'SmsPart'
        db.delete_table(u'sms_smspart')


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
            'sms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sms.Sms']"})
        }
    }

    complete_apps = ['sms']