from django.urls import path
from . import views

urlpatterns=[
    path('db',views.admin_template, name="admin_template"),
    path('', views.init_template, name="init_template"),
    path('home/', views.home_template, name="home_template"),
    path('<int:term>/<int:day>/<int:time>/list/', views.day_list_template, name="day_list_template"),
    path('<int:tire>/<int:class_id>/more/', views.more_template, name="more_template")
]