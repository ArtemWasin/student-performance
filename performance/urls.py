from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_create, name='subject_create'),
    path('subjects/edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_create, name='grade_create'),
    path('grades/edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('grades/delete/<int:pk>/', views.grade_delete, name='grade_delete'),
    path('reports/', views.reports, name='reports'),
]