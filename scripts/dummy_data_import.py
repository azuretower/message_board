#!/usr/bin/env python
import requests
import sys
import os
import csv

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Message
from django.contrib.auth.models import User

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dummy_data.csv")
csv_file = open(csv_file_path, 'r')
reader = csv.DictReader(csv_file)

user = User.objects.get(username='admin')

for row in reader:
    new_message = Message.objects.create(author=user)
    new_message.text = row['text']
    new_message.title = row['title']
    new_message.save()
