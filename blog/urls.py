from django.urls import path
from . import  views

urlpatterns = [
    path('', views.post_list, name='post'),
    path('123', views.post_test,name='test')
]