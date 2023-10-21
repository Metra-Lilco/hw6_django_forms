from django.urls import path

from .views import teacher_form


urlpatterns = [
   path("teacher", teacher_form, name="teacher_form") 
]
