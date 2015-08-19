# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20150817_1336'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='Login_users',
        ),
    ]
