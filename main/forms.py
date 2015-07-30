from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
