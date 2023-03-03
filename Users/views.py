from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import *

# Create your views here.
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, 
                            username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('Events_listV')   
    return render(request, 'users/login.html', {'form': form})