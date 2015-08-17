# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_num', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('user_pwd', models.CharField(max_length=50)),
                ('user_role', models.IntegerField()),
                ('user_hospital', models.CharField(max_length=50)),
            ],
        ),
    ]
