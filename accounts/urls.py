from django.urls import path
from . import views

url_patterns = [
    path("register/",view=views.createNewUser,name="register user")
]

