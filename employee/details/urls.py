from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.base,name="base"),
    path('create',views.create,name='create'),


    path('list',views.listt,name='list'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>',views.deletee,name='delete')
    
   
]