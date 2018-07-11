from django.urls import path
from . import views

#应用sqltest内部的url地址设置
urlpatterns=[
    path('', views.display, name= 'display')
]

