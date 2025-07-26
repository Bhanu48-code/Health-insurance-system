from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyApp, Myemployee, MyadminUsers

# Create your views here.
def login(request):
   # return HttpResponse("welcome bhanu!!!! Great work.")
   
    if (request.method == 'POST'):
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
       
         # You can now validate credentials or authenticate the user
        try:
            
             user = MyApp.objects.get(username=username, password=password)
             return render(request, 'adminHome.html')
             #return render(request, 'welcome.html', {'user': user.username})
            
        except MyApp.DoesNotExist:
            return HttpResponse("Invalid username or password")
           
    return render(request, 'login.html')
   #return render(request, 'home.html')


# customer or employee options login 
def loginChoice(request):
    return render(request,"HomePage.html")



def newRegisterForm(request):
   
   return render(request,"registration_form.html")
  
   
  
def newRegistration(request):
    if request.method == 'POST':
        create_username = request.POST.get('create_new_username')
        create_password = request.POST.get('create_new_password')
        create_confirm_password = request.POST.get('create_confirm_password')

        

        if create_password == create_confirm_password:
             

            try:
               MyApp.objects.create(username=create_username, password=create_password)
               #return render(request,"registration_status.html")
               return HttpResponse("register successfully")
               return render(request,"login.html")
              
            except Exception as e:
               return HttpResponse(f"Error: {e}")
               return render(request, "Registration_successfull.html", {"username": create_password})
               # Save the data to MySQL via Django model
             
            
        else:
            return render(request, "Registration_successfull.html", {"username": "Passwords do not match."})


def show_users(request):
    users = MyApp.objects.all()
    return render(request, 'users.html', {'users': users})

   
   



#below all code belongs to employee creation and registration 
def employeeNewRegistration(request):
   return render(request,"New_Employee_registration.html")

def employeelogin(request):
    return render(request,"employee_login.html")

def employeeDetailsRegistration(request):
    if request.method == 'POST':
        emp_name = request.POST.get('create_emp_name')
        emp_email = request.POST.get('create_emp_email')
        emp_Password = request.POST.get('new_emp_password')

        if emp_name and emp_email and emp_Password:
             

            try:
               Myemployee.objects.create(name=emp_name, email=emp_email, password=emp_Password)
               return render(request,"employee_login.html")
               
               return HttpResponse("register successfully")
               #return render(request,"login.html")
              
            except Exception as e:
               return HttpResponse(f"Error: {e}")
               return render(request, "Registration_successfull.html", {"username": create_password})
               # Save the data to MySQL via Django model

#employee login vaidtion for admin access 
def employeeValidation(request):
     if request.method == 'POST':
         Emp_login_mail_Id = request.POST.get("EMP_Email_ID")
         Emp_login_password = request.POST.get("EMP_Password")
         if MyadminUsers.objects.filter(email=Emp_login_mail_Id, AdminPassword=Emp_login_password).exists():
             #validating the credentils present present in Admin table or not 
             user = MyadminUsers.objects.get(email=Emp_login_mail_Id, AdminPassword=Emp_login_password)
             return render(request,"adminHome.html")
         elif Myemployee.objects.filter(email=Emp_login_mail_Id, password=Emp_login_password).exists():
             return render(request,"NonAdminEmployeLogin.html")
         else:
             return HttpResponse("Wrong credentials no access is available for you")
    
# below method is for giving admin access for new admin user
def giveAccessForAdminRole(request):
    if request.method == 'POST':
        New_adminUser_Email_Id = request.POST.get("NewAdminEmail")
        New_adminUser_Password = request.POST.get("NewAdminPassword")
        if MyadminUsers.objects.filter(email=New_adminUser_Email_Id).exists():
            return render(request,"adminHome.html")
        else:
            # If not exists, create new admin user
            MyadminUsers.objects.create(email=New_adminUser_Email_Id, AdminPassword=New_adminUser_Password)
            return render(request, "adminHome.html")
        

        

    
    



