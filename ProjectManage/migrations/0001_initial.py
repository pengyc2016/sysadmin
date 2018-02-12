# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResourceManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clustername', models.CharField(unique=True, max_length=30, verbose_name='\u96c6\u7fa4\u540d\u79f0', db_index=True)),
                ('platform', models.CharField(max_length=30, verbose_name='\u96c6\u7fa4\u5e73\u53f0')),
                ('vcaddress', models.GenericIPAddressField(verbose_name='\u96c6\u7fa4VC\u5730\u5740')),
                ('ttstorage', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5b58\u50a8', blank=True)),
                ('usedstorage', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5b58\u50a8', blank=True)),
                ('systorage', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5b58\u50a8', blank=True)),
                ('ttcore', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4CPU\u6838\u6570', blank=True)),
                ('usedcore', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528CPU\u6838\u6570', blank=True)),
                ('sycore', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59CPU\u6838\u6570', blank=True)),
                ('ttmem', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5185\u5b58', blank=True)),
                ('usedmem', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5185\u5b58', blank=True)),
                ('symem', models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5185\u5b58', blank=True)),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('storagegroup', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u96c6\u7fa4\u5b58\u50a8\u7ec4', to='ResourceManage.StorageGroup', null=True)),
                ('vlangroup', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u96c6\u7fa4\u7f51\u7edc\u7ec4', to='ResourceManage.VlanGroup', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'cluster',
            },
        ),
        migrations.CreateModel(
            name='Pm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pmname', models.CharField(unique=True, max_length=30, verbose_name='\u7269\u7406\u673a\u540d\u79f0', db_index=True)),
                ('sn', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u5e8f\u5217\u53f7', blank=True)),
                ('role', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u89d2\u8272', blank=True)),
                ('type', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u7c7b\u578b', blank=True)),
                ('cpu', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673aCPU\u6838\u6570', blank=True)),
                ('memory', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u5185\u5b58\u5927\u5c0f', blank=True)),
                ('disk', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u78c1\u76d8\u5927\u5c0f', blank=True)),
                ('os', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u64cd\u4f5c\u7cfb\u7edf', blank=True)),
                ('eth', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u7f51\u5361\u4e2a\u6570', blank=True)),
                ('hba', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673aHBA\u5361\u4e2a\u6570', blank=True)),
                ('ip', models.GenericIPAddressField(verbose_name='\u7269\u7406\u673a\u5730\u5740')),
                ('ilo_ip', models.GenericIPAddressField(verbose_name='\u7269\u7406\u673a\u7ba1\u7406\u5730\u5740')),
                ('mask', models.GenericIPAddressField(null=True, verbose_name='\u7269\u7406\u673a\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('gateway', models.GenericIPAddressField(null=True, verbose_name='\u7269\u7406\u673a\u7f51\u5173', blank=True)),
                ('jiguihao', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u673a\u67dc\u53f7', blank=True)),
                ('jiguiwei', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u673a\u67dc\u4f4d', blank=True)),
                ('hba_wwn', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673aHBA\u5361WWN', blank=True)),
                ('position', models.CharField(max_length=30, null=True, verbose_name='\u7269\u7406\u673a\u4f4d\u7f6e', blank=True)),
                ('ttstorage', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u5b58\u50a8\u5927\u5c0f', blank=True)),
                ('systorage', models.IntegerField(null=True, verbose_name='\u5269\u4f59\u5b58\u50a8\u5927\u5c0f', blank=True)),
                ('sycore', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u5269\u4f59CPU\u6838\u6570', blank=True)),
                ('symem', models.IntegerField(null=True, verbose_name='\u7269\u7406\u673a\u5269\u4f59CPU\u6838\u6570', blank=True)),
                ('remark', models.CharField(max_length=30, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u96c6\u7fa4', blank=True, to='ProjectManage.Cluster', null=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u57df', blank=True, to='ResourceManage.Domain', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'pm',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('env', models.CharField(max_length=30, null=True, verbose_name='\u73af\u5883', blank=True)),
                ('projectname', models.CharField(max_length=30, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('shortname', models.CharField(max_length=30, null=True, verbose_name='\u9879\u76ee\u7b80\u79f0', blank=True)),
                ('starttime', models.DateTimeField(null=True, verbose_name='\u9879\u76ee\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('endtime', models.DateTimeField(null=True, verbose_name='\u9879\u76ee\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('finishtime', models.DateTimeField(null=True, verbose_name='\u9879\u76ee\u5b8c\u6210\u65f6\u95f4', blank=True)),
                ('reason', models.CharField(max_length=200, null=True, verbose_name='\u9879\u76ee\u8d85\u65f6\u7406\u7531', blank=True)),
                ('batch', models.CharField(max_length=10, null=True, verbose_name='\u9879\u76ee\u6279\u6b21', blank=True)),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('createuser', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u521b\u5efa\u4eba\u5458', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vmname', models.CharField(unique=True, max_length=30, verbose_name='\u865a\u62df\u673a\u540d\u79f0', db_index=True)),
                ('role', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u89d2\u8272', blank=True)),
                ('batch', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u6279\u6b21', blank=True)),
                ('env', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u73af\u5883', blank=True)),
                ('os', models.CharField(max_length=80, verbose_name='\u865a\u62df\u673a\u64cd\u4f5c\u7cfb\u7edf')),
                ('cpu', models.IntegerField(null=True, verbose_name='\u865a\u62df\u673acpu\u6838\u6570', blank=True)),
                ('mem', models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u5185\u5b58\u5927\u5c0f', blank=True)),
                ('disk', models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u78c1\u76d8\u5927\u5c0f', blank=True)),
                ('ip', models.GenericIPAddressField(verbose_name='\u865a\u62df\u673a\u5730\u5740')),
                ('mask', models.GenericIPAddressField(null=True, verbose_name='\u865a\u62df\u673a\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('gateway', models.GenericIPAddressField(null=True, verbose_name='\u865a\u62df\u673a\u7f51\u5173', blank=True)),
                ('admin', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u7ba1\u7406\u5458', blank=True)),
                ('appuser', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u5e94\u7528\u7528\u6237', blank=True)),
                ('uptime', models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u542f\u52a8\u65f6\u95f4', blank=True)),
                ('vmstatus', models.BooleanField(default=False, verbose_name='\u865a\u62df\u673a\u72b6\u6001')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u96c6\u7fa4', blank=True, to='ProjectManage.Cluster', null=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u865a\u62df\u673a\u6240\u5c5e\u57df', blank=True, to='ResourceManage.Domain', null=True)),
                ('pm', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u7269\u7406\u673a', blank=True, to='ProjectManage.Pm', null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u9879\u76ee', blank=True, to='ProjectManage.Project', null=True)),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u865a\u62df\u673a\u5b89\u88c5\u8f6f\u4ef6', blank=True, to='ResourceManage.Software', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'vm',
            },
        ),
        migrations.AddField(
            model_name='pm',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u9879\u76ee', blank=True, to='ProjectManage.Project', null=True),
        ),
        migrations.AddField(
            model_name='pm',
            name='soft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u5b89\u88c5\u8f6f\u4ef6', blank=True, to='ResourceManage.Software', null=True),
        ),
        migrations.AddField(
            model_name='pm',
            name='storagegroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u5b58\u50a8\u7ec4', blank=True, to='ResourceManage.StorageGroup', null=True),
        ),
        migrations.AddField(
            model_name='pm',
            name='vlangroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u7f51\u7edc\u7ec4', blank=True, to='ResourceManage.VlanGroup', null=True),
        ),
    ]
