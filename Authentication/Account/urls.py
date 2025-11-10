'''
Docstring for Projects.Authentication.Account.urls
'''
from django.urls import path,include
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView,name='signup'),
    path('',include('django.contrib.auth.urls')),
]
