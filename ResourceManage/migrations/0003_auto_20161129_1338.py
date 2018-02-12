# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0002_auto_20161125_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tongji',
            name='count',
            field=models.IntegerField(null=True, verbose_name='\u6570\u91cf', blank=True),
        ),
    ]
