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
    student_edit,
    teacher_edit,
    group_edit,
    student_delete,
    group_delete,
    teacher_delete,
)


urlpatterns = [
    path("", index, name="index"),
    path("university", university, name="university"),
    path("teacher", teacher_form, name="teacher_form"),
    path("teachers", teachers_list, name="teachers_list"),
    path("teacher/<int:pk>", teacher_edit, name="teacher_edit"),
    path("teacher/<int:pk>/delete", teacher_delete, name="teacher_delete"),
    path("group", group_form, name="group_form"),
    path("groups", groups_list, name="groups_list"),
    path("student", student_form, name="student_form"),
    path("students", students_list, name="students_list"),
    path("student/<int:pk>", student_edit, name="student_edit"),
    path("student/<int:pk>/delete", student_delete, name="student_delete"),
    path("group/<int:pk>", group_edit, name="group_edit"),
    path("group/<int:pk>/delete", group_delete, name="group_delete"),
]
