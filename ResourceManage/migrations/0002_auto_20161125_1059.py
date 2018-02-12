# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='storagesize',
            field=models.DecimalField(verbose_name='\u5b58\u50a8\u5927\u5c0f', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='storagegroup',
            name='systorage',
            field=models.DecimalField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5269\u4f59\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='storagegroup',
            name='ttstorage',
            field=models.DecimalField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='storagegroup',
            name='usedstorage',
            field=models.DecimalField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5df2\u7528\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tongji',
            name='count',
            field=models.DecimalField(null=True, verbose_name='\u7edf\u8ba1\u7c7b\u578b', max_digits=8, decimal_places=2, blank=True),
        ),
    ]
