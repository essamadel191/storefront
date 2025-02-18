# Maping
from django.urls import path
from . import views


# URLConf
urlpatterns = [
    # View.say_hello without parenthesis () as we are just passing
    # to this funcation 
    path('hello/', views.say_hello)
]
