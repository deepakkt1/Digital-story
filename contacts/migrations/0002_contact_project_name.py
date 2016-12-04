# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='project_name',
            field=models.CharField(default=datetime.datetime(2016, 10, 18, 3, 5, 37, 888122, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
