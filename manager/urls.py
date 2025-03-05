from django.urls import path
from . import views

urlpatterns=[
    path('', views.init_template, name="init_template"),
    path('home/', views.home_template, name="home_template"),
    path('more/', views.more_template, name="more_template")
]