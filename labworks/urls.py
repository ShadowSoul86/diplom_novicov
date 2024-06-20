from django.urls import path
from . import views

urlpatterns = [
    path('', views.labwork_list, name='labwork_list'),
    path('<slug:slug>/', views.labwork_detail, name='labwork_detail'),
]
