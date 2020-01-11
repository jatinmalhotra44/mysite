from django.shortcuts import render
from django.http import HttpResponse
from basicapp.forms import UserForm,ProfileForm
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')


def reg(request):
    registered=False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        profile_form= ProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()

            profile= profile_form.save(commit=False)
            profile.user=user

            if 'pic' in request.FILES:
                profile.pic=request.FILES['pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors)
    else:
            user_form=UserForm()
            profile_form=ProfileForm()
    

    return render(request,'basicapp/register.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

