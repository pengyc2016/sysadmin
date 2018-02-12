# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0003_auto_20161125_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='disk',
            field=models.DecimalField(null=True, verbose_name='\u865a\u62df\u673a\u78c1\u76d8\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='mem',
            field=models.DecimalField(null=True, verbose_name='\u865a\u62df\u673a\u5185\u5b58\u5927\u5c0f', max_digits=8, decimal_places=2, blank=True),
        ),
    ]
