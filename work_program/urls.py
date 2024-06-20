from django.urls import path
from . import views

urlpatterns = [
    path('work_program/', views.work_program_view, name='work_program'),
    path('work_program/pdf/<str:pdf_name>/', views.pdf_view, name='pdf_view'),
]
