# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_message_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='favorite',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
