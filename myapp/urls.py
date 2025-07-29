from django.urls import path
from . import views

urlpatterns = [
     path('', views.loginChoice, name='home'),         # root URL
    # below are for customer related links
    path('customerLogin/',views.login,name='home'),
    path('newRegisterForm/',views.newRegisterForm,name='New_registration_form'),
    path('newRegistration/',views.newRegistration,name='New_Registration'),
     path('show-users/', views.show_users, name='show_users'),

     

     #below all are for employee related 
     path("employeeLogin/",views.employeelogin,name="emplogin"),
     path("newEmployeeRegistration/",views.employeeNewRegistration,name="employeenewregistration"),
     path("newempDetailsRegistration/",views.employeeDetailsRegistration,name="employeeDetailsRegistration"),
     path("employeeValidation/",views.employeeValidation,name="employeeValidation"),
     path("giveAccess/",views.giveAccessForAdminRole,name="giveAccessForAdminRole"),


]