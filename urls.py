from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('adminpanel/', views.admin_panel, name='adminpanel'),
    path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit-student'),
    path('edit-confirm/<int:id>/', views.edit_confirm, name='edit-confirm'),
    path('logout/', views.admin_logout, name='admin-logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_confirm/', views.add_confirm, name='add_confirm'),
]

