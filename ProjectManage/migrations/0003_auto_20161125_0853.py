# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0002_auto_20161124_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm',
            name='arch',
            field=models.CharField(max_length=30, null=True, verbose_name='\u7cfb\u7edf\u67b6\u6784', blank=True),
        ),
        migrations.AddField(
            model_name='vm',
            name='diskmount',
            field=models.CharField(max_length=200, null=True, verbose_name='\u78c1\u76d8\u6302\u8f7d\u4fe1\u606f', blank=True),
        ),
        migrations.AddField(
            model_name='vm',
            name='kernel',
            field=models.CharField(max_length=100, null=True, verbose_name='\u7cfb\u7edf\u5185\u6838\u7248\u672c', blank=True),
        ),
        migrations.AddField(
            model_name='vm',
            name='pycpu',
            field=models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u7269\u7406cpu\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='cpu',
            field=models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u903b\u8f91cpu\u6838\u6570', blank=True),
        ),
    ]
