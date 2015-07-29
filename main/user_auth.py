from django.contrib.auth.models import User, Group
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm


