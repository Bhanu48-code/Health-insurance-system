from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyApp, Myemployee

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
        create_emp_name = request.POST.get('create_emp_name')
        create_emp_email = request.POST.get('create_emp_email')
        

        

        if create_emp_name and create_emp_email:
             

            try:
               Myemployee.objects.create(name=create_emp_name, email=create_emp_email)
               
               return HttpResponse("register successfully")
               #return render(request,"login.html")
              
            except Exception as e:
               return HttpResponse(f"Error: {e}")
               return render(request, "Registration_successfull.html", {"username": create_password})
               # Save the data to MySQL via Django model
    
    



