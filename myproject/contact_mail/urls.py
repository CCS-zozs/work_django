# contact_mail/urls.py
from django.urls import path
from . import views

app_name = 'contact_mail'

urlpatterns = [
    path('', views.send_email_view, name='index'),
]