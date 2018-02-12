# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0004_auto_20161209_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='softwarefullname',
            field=models.CharField(max_length=50, null=True, verbose_name='\u8f6f\u4ef6\u5168\u540d', blank=True),
        ),
    ]
