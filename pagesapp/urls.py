from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='Home'),
    path('about/', views.AboutMePage.as_view(), name='About')
]