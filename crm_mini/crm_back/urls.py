from django.contrib import admin
from django.urls import path

from . import views

app_name = 'back'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_group/', views.create_group, name='create_group'),
    path('group_list/', views.group_list, name='group_list'),
    path('group_detail/<int:id>/', views.group_detail, name='group_detail'),
    path('student_detail/<int:id>/', views.student_detail, name='student_detail'),
    path('date_selection/', views.date_selection, name='date_selection'),
    path('students_list/', views.students_list, name='students_list'),
    path('download_data/', views.download_data, name='download_data'),
]
