from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from roommate_app.backend.models import UserProfile

def register_user(username, email, password):
    user = User.objects.create_user(username, email, password)
    user.save()

def login_user(username, password):
    user = User.objects.authenticate(username, password)
    if user is not None:
        login(user)
        return True
    else:
        return False

def get_user_profile(user):
    profile = UserProfile.objects.get(user=user)
    return profile

def update_user_profile(user, profile):
    profile.user = user
    profile.save()