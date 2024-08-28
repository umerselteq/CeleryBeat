from django.urls import path
from . import views
app_name = 'my_celery_app'

urlpatterns = [
    path('add/', views.adding, name='add'),
    path('result/', views.check_task_status, name='check_task_status'),
    path('create/', views.CandidateSet.as_view(), name='Candidate-set'),
]