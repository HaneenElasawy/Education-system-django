from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Students
    path('students/', views.students_page, name='students'),
    path('students/edit/<str:slug>/', views.edit_student, name='edit_student'),
    path('students/delete/<str:slug>/', views.delete_student, name='delete_student'),

    # Subjects
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/edit/<str:slug>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<str:slug>/', views.delete_subject, name='delete_subject'),

    # Grades
    path('grades/', views.grades_page, name='grades'),
    path('grades/edit/<int:id>/', views.edit_grade, name='edit_grade'),
    path('grades/delete/<int:id>/', views.delete_grade, name='delete_grade'),

    # Profile
    path('profile/', views.profile_page, name='profile'),

    # Contact
    path('contact/', views.contact_page, name='contact'),
    
    #Leaderboard
    path('leaderboard/', views.leaderboard_page, name='leaderboard'),

]