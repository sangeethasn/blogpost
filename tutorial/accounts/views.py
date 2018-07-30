from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm



def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()

    args={'form':form}
    return render(request,'accounts/reg_form.html',args)