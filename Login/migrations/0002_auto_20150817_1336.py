# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_role',
            field=models.IntegerField(help_text=b'1:\xe9\x87\x87\xe9\x9b\x86\xe5\x8c\xbb\xe7\x94\x9f;2:\xe8\xaf\x8a\xe6\x96\xad\xe5\x8c\xbb\xe7\x94\x9f'),
        ),
    ]
