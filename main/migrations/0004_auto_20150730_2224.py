# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='favorite',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
