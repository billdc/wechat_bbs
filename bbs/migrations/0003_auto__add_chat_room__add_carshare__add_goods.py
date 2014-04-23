# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chat_room'
        db.create_table(u'bbs_chat_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('messages', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bbs', ['Chat_room'])

        # Adding model 'CarShare'
        db.create_table(u'bbs_carshare', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('from_addr', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('to_addr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'bbs', ['CarShare'])

        # Adding model 'Goods'
        db.create_table(u'bbs_goods', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dist', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'bbs', ['Goods'])


    def backwards(self, orm):
        # Deleting model 'Chat_room'
        db.delete_table(u'bbs_chat_room')

        # Deleting model 'CarShare'
        db.delete_table(u'bbs_carshare')

        # Deleting model 'Goods'
        db.delete_table(u'bbs_goods')


    models = {
        u'bbs.carshare': {
            'Meta': {'object_name': 'CarShare'},
            'from_addr': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'to_addr': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bbs.chat_room': {
            'Meta': {'object_name': 'Chat_room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'bbs.goods': {
            'Meta': {'object_name': 'Goods'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dist': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'bbs.house': {
            'Meta': {'object_name': 'House'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dist': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bbs']