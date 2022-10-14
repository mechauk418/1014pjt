from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.

def index(request):

    accounts = User.objects.order_by('pk')

    context = {
        'accounts':accounts
    }   

    

    return render(request,'accounts/index.html',context)

def signup(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
        
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()

    context={
        'form':form
    }

    return render(request,'accounts/signup.html',context)