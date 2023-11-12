from django.urls import path

from .views import (
    teacher_form,
    group_form,
    teachers_list,
    groups_list,
    index,
    university,
    student_form,
    students_list,
)


urlpatterns = [
    path("", index, name="index"),
    path("university", university, name="university"),
    path("teacher", teacher_form, name="teacher_form"),
    path("teachers", teachers_list, name="teachers_list"),
    path("teacher/<int:pk>", teacher_form, name="teacher_edit"),
    path("group", group_form, name="group_form"),
    path("groups", groups_list, name="groups_list"),
    path("student", student_form, name="student_form"),
    path("students", students_list, name="students_list"),
    path("student/<int:pk>", student_form, name="student_edit"),
]
