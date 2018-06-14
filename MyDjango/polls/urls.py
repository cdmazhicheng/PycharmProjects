from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('indexone', views.index_one, name= 'indexone'),
    path('indextwo', views.index_two, name= 'indextwo'),
    path('indexthree', views.index_three, name='indexthree'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name= 'detail'),
]
