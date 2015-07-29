# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default=b"i can't think of a title", max_length=255),
        ),
    ]
