from django.urls import path
from . import  views

urlpatterns = [
    path('hold_on/', views.post_list, name='post'),
    path('getin/', views.post_test,name='test')
]