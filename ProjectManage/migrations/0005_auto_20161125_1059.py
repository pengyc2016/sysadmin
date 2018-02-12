# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0004_auto_20161125_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='symem',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5185\u5b58', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='systorage',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5b58\u50a8', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttmem',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5185\u5b58', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttstorage',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5b58\u50a8', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='usedmem',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5185\u5b58', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='usedstorage',
            field=models.DecimalField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5b58\u50a8', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='disk',
            field=models.DecimalField(null=True, verbose_name='\u7269\u7406\u673a\u78c1\u76d8\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='memory',
            field=models.DecimalField(null=True, verbose_name='\u7269\u7406\u673a\u5185\u5b58\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='systorage',
            field=models.DecimalField(null=True, verbose_name='\u5269\u4f59\u5b58\u50a8\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='ttstorage',
            field=models.DecimalField(null=True, verbose_name='\u7269\u7406\u673a\u5b58\u50a8\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
    ]
