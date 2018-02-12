# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0005_auto_20161125_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm',
            name='scan',
            field=models.GenericIPAddressField(null=True, verbose_name='\u865a\u62df\u673aSCAN\u5730\u5740', blank=True),
        ),
        migrations.AddField(
            model_name='vm',
            name='vip',
            field=models.GenericIPAddressField(null=True, verbose_name='\u865a\u62df\u673aVIP\u5730\u5740', blank=True),
        ),
    ]
