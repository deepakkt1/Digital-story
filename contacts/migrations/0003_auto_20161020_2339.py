# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_project_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Faculty_email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='Faculty_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='Faculty_phone_number',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='project_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='Faculty_department_or_program',
            field=models.CharField(default=datetime.datetime(2016, 10, 20, 23, 39, 46, 697877, tzinfo=utc), max_length=12, choices=[(b'AER', b'Aerospace Engineering Sciences '), (b'APM', b'Applied Math'), (b'CBE', b'Chemical & Biological Engineering'), (b'CEA', b'Civil, Environmental & Architectural Engineering '), (b'CSE', b'Computer Science'), (b'ECE', b'Electrical, Computer & Energy Engineering'), (b'Phy', b'Physics'), (b'EEn', b'Environmental Engineering'), (b'MEn', b'Mechanical Engineering'), (b'CSG', b'Colorado Space Grant'), (b'EnE', b'Engineering Education'), (b'ATL', b'ATLAS')]),
            preserve_default=False,
        ),
    ]
