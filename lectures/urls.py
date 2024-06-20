from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecture_list, name='lecture_list'),
    path('<slug:slug>/', views.lecture_detail, name='lecture_detail'),
]
