from django.urls import path
from demoApp import views

urlpatterns = [
    path('get', views.getClients, name='getClients'),
    path('insert', views.insertClient, name='insertClient'),
    path('update/<id>', views.updateClient, name='updateClient'),
    path('delete/<id>', views.deleteClient, name='deleteClient'),
]
