from django.urls import path
from . import views

urlpatterns = [
    path("register/",view=views.registerNewUser,name="register user"),
    path("log-in/",view=views.userLogin,name="user login")
]

