from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm

def home(request):
    numbers =[1,2,3,4,5]
    name ='Sangeetha'

    args ={'myName': name,'number': numbers}

    return render(request,'accounts/home.html')

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
    asd='jyfuj'
    args={'form':form}
    return render(request,'accounts/reg_form.html',args)