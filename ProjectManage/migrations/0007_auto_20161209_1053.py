# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0006_auto_20161201_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pm',
            old_name='type',
            new_name='pmtype',
        ),
    ]
