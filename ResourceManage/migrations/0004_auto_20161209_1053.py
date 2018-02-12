# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0003_auto_20161129_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software',
            old_name='type',
            new_name='softtype',
        ),
    ]
