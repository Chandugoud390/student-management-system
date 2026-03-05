from .import views
from . import ajax_views
from django.urls import path

app_name = 'students'

urlpatterns = [
    path("list/", views.student_list, name="student_list"),    
    path("create/", views.student_create, name="student_create"),    
    path("<uuid:pk>/update/", views.student_edit, name="student_edit"),    
    path("<uuid:pk>/delete/", views.student_delete, name="student_delete"), 
    path("<uuid:pk>/Profile/", views.student_profile, name="student_profile"),

    # Ajax End points
    path("ajax/update-profile-picture/", ajax_views.update_student_profile_picture, name="ajax_update_student_profile_picture")   
]