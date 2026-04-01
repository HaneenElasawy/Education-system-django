from django.urls import path
from .api_views import (
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    subject_list_create,
    subject_detail,
    GradeListCreateAPIView,     
    GradeRetrieveUpdateDestroyAPIView,  
    RegisterAPIView,
    LoginAPIView, 
)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve-update-destroy'),
    path('subjects/', subject_list_create, name='subject-list-create'),
    path('subjects/<int:pk>/', subject_detail, name='subject-retrieve-update-destroy'),
    path('grades/', GradeListCreateAPIView.as_view(), name='grade-list-create'),
    path('grades/<int:pk>/', GradeRetrieveUpdateDestroyAPIView.as_view(), name='grade-retrieve-update-destroy'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]   