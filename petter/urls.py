from django.urls import path
from . import views

app_name = 'petter'

urlpatterns = [
    path('', views.main, name='main'),
]
