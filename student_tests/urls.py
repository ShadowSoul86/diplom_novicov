from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('<slug:test_slug>/', views.start_test, name='start_test'),
    path('<slug:test_slug>/questions/<int:question_id>/',
         views.question_detail, name='question_detail'),
    path('submit_test/<slug:test_slug>/',
         views.submit_test, name='submit_test'),
    path('test_result/<int:score>/', views.test_result, name='test_result'),
    path('test_results/', views.test_results, name='test_results'),
]
