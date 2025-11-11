from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your views here.
def register_page(request):
    '''
    Docstring for register_page
    
    :param request: Description
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'User With Username Already Exist')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password=password
            )
        messages.info(request,'User Successfuly Created')
        return redirect('register')
    return render(request,'register.html')


def login_view(request):
    '''
    Docstring for login
    
    :param request: Description
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            messages.info(request,'User Successfuly Login')
            return redirect('login')
        messages.info(request,'Invalid Credential')
        return redirect('login')
    return render(request,'login.html')
