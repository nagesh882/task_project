from django.urls import path
from student import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('home/', views.home, name='home'),
]
