from django.urls import path
from . import views

urlpatterns = [
     path('', views.loginChoice, name='home'),         # root URL
    
    path('customerLogin/',views.login,name='home'),
    path('newRegisterForm/',views.newRegisterForm,name='New_registration_form'),
    path('newRegistration/',views.newRegistration,name='New_Registration'),
     path('show-users/', views.show_users, name='show_users'),
]