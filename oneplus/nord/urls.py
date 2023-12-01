from django.urls import path
from nord import views

urlpatterns = [
    path('', views.form, name='form'),
    path('data/', views.data, name='data')
]