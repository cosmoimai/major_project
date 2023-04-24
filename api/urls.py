from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('form/', views.get_form),
    path('home/', views.home),
    path('process', views.get_form_response)
]