from django.urls import path
from .import views

urlpatterns = [
    path('',views.first_login, name='first_login')
]