from django.urls import path,include
from .views import register_page,login_view

urlpatterns = [
    # path('account/',include('django.contrib.auth.urls')),
    path('account/',register_page,name='register'),
    path('account/login/',login_view,name='login'),
]
