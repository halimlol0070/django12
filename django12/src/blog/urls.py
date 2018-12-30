'''
Created on 2018. 12. 29.

@author: user
'''
app_name='blog'
from django.urls import path
from .views import *
urlpatterns=[
   path('',Index.as_view(),name='index'),
   path('<int:pk>/',Detail.as_view(),name='detail'),
   path('postP/',PostRegister.as_view(), name='postP'),
   path('search/',Searchp.as_view(), name='searchP'),
   
    
    
    ]