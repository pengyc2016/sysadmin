# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='uptime',
            field=models.CharField(max_length=30, null=True, verbose_name='\u865a\u62df\u673a\u5df2\u542f\u52a8\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='vmstatus',
            field=models.BooleanField(default=False, verbose_name='\u865a\u62df\u673a\u5f00\u673a\u72b6\u6001'),
        ),
    ]
