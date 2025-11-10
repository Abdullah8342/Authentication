from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def SignUpView(request):
    '''
    Docstring for SignUpView
    
    :param request: Description
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
