from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "GesPerson"
urlpatterns = [
    path('', views.index, name='index'),
    path("add_teacher", views.add_teacher, name='add_teacher'),
    path("teachers/show_t", views.show_t, name='show_t'),
    path('teachers/edit/<int:id>', views.edit, name='edit'),

    path("add_student", views.add_student, name='add_student'),
    path("students/show_s", views.show_s, name='show_s'),
    path('students/edit_s/<int:id>', views.edit_s, name='edit_s'),


]
