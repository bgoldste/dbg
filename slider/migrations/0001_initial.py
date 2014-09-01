# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'slider_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'slider', ['Slide'])

        # Adding model 'Contact'
        db.create_table(u'slider_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'slider', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'slider_slide')

        # Deleting model 'Contact'
        db.delete_table(u'slider_contact')


    models = {
        u'slider.contact': {
            'Meta': {'object_name': 'Contact'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'slider.slide': {
            'Meta': {'object_name': 'Slide'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['slider']