# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0008_auto_20180118_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='disk',
            field=models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u78c1\u76d8\u5927\u5c0f', blank=True),
        ),
    ]
