from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Course, Material
from .forms import OrderForm

def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Order Confirmed")
    else:
        form = OrderForm()

    return render(request, 'home.html', {'form': form})

def get_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id)
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})

# Create your views here.
def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"Email Taken")
            #     return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,)
                user.save()
                return redirect('login')


        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

# def form(request):
#     return render(request,'home.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
