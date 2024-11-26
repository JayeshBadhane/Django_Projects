from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about_us/", views.about, name="about_us"),
    path('service/', views.service, name='service'),  # Fixed typo
    path('contact_us/', views.contact, name='contact_us'),
    path('sum/', views.Sum, name='sum'),
    path('student/', views.sud, name='student'),
    path('result/', views.msheet, name='result'),
    path('employee/', views.employeePage, name='employee'),
    path('employeeData/', views.employeeDataSave, name='employeeData'),
    path('edit_emp/<int:id>/', views.editEmployeeData, name='edit_emp'),
]
