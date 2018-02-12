# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domainname', models.CharField(unique=True, max_length=30, verbose_name='\u57df\u540d\u79f0', db_index=True)),
                ('DNS', models.GenericIPAddressField(verbose_name='DNS')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'domain',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('softwarename', models.CharField(max_length=30, verbose_name='\u8f6f\u4ef6\u540d\u79f0')),
                ('version', models.CharField(max_length=30, verbose_name='\u8f6f\u4ef6\u7248\u672c')),
                ('platform', models.CharField(max_length=30, verbose_name='\u8f6f\u4ef6\u5e73\u53f0')),
                ('arch', models.CharField(max_length=10, verbose_name='\u8f6f\u4ef6\u67b6\u6784')),
                ('doc', models.CharField(max_length=100, null=True, verbose_name='\u8f6f\u4ef6\u5b89\u88c5\u6587\u6863', blank=True)),
                ('path', models.CharField(max_length=100, null=True, verbose_name='\u8f6f\u4ef6\u5b58\u50a8\u8def\u5f84', blank=True)),
                ('type', models.CharField(max_length=30, verbose_name='\u7c7b\u578b')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'software',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storagename', models.CharField(unique=True, max_length=100, verbose_name='\u5b58\u50a8\u540d\u79f0', db_index=True)),
                ('storagesize', models.IntegerField(verbose_name='\u5b58\u50a8\u5927\u5c0f')),
                ('storagetype', models.CharField(max_length=30, verbose_name='\u5b58\u50a8\u7c7b\u578b')),
                ('raidtype', models.CharField(max_length=30, verbose_name='\u5b58\u50a8RAID\u7c7b\u578b')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'storage',
            },
        ),
        migrations.CreateModel(
            name='StorageGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storagegroupname', models.CharField(unique=True, max_length=30, verbose_name='\u5b58\u50a8\u7ec4\u540d\u79f0', db_index=True)),
                ('ttstorage', models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5927\u5c0f', blank=True)),
                ('systorage', models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5269\u4f59\u5927\u5c0f', blank=True)),
                ('usedstorage', models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5df2\u7528\u5927\u5c0f', blank=True)),
                ('is_selected', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u7528')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'storagegroup',
            },
        ),
        migrations.CreateModel(
            name='Tongji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tongjitype', models.CharField(unique=True, max_length=50, verbose_name='\u7edf\u8ba1\u7c7b\u578b', db_index=True)),
                ('count', models.IntegerField(null=True, verbose_name='\u7edf\u8ba1\u7c7b\u578b', blank=True)),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'tongji',
            },
        ),
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vlanname', models.GenericIPAddressField(unique=True, verbose_name='\u7f51\u6bb5\u540d\u79f0', db_index=True)),
                ('startip', models.IntegerField(default=16, verbose_name='\u7f51\u6bb5\u8d77\u59cbIP')),
                ('endip', models.IntegerField(default=254, verbose_name='\u7f51\u6bb5\u7ed3\u675fIP')),
                ('gateway', models.GenericIPAddressField(verbose_name='\u7f51\u6bb5\u7f51\u5173')),
                ('mask', models.GenericIPAddressField(verbose_name='\u7f51\u6bb5\u63a9\u7801')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'vlan',
            },
        ),
        migrations.CreateModel(
            name='VlanGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vlangroupname', models.CharField(unique=True, max_length=30, verbose_name='\u7f51\u6bb5\u7ec4\u540d\u79f0', db_index=True)),
                ('ttip', models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4IP\u4e2a\u6570', blank=True)),
                ('syip', models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4\u5269\u4f59IP\u4e2a\u6570', blank=True)),
                ('usedip', models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4\u5df2\u7528IP\u4e2a\u6570', blank=True)),
                ('is_selected', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u7528')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('vlan', models.ManyToManyField(to='ResourceManage.Vlan', verbose_name='\u7f51\u6bb5\u540d\u79f0', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'vlangroup',
            },
        ),
        migrations.AddField(
            model_name='storage',
            name='storagegroup',
            field=models.ForeignKey(verbose_name='\u5b58\u50a8\u7ec4\u540d\u79f0', to='ResourceManage.StorageGroup'),
        ),
    ]
