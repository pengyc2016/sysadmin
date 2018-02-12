# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0007_auto_20161209_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='mem',
            field=models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u5185\u5b58\u5927\u5c0f', blank=True),
        ),
    ]
