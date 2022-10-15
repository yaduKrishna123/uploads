from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django .contrib.auth.decorators import login_required


# Create your views here.
# def demo(request):
#     return render(request,'base.html')
from django.utils.datastructures import MultiValueDictKeyError

from starapp.forms import updateforms
from starapp.models import Upload


def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new_uploads')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,'login.html')

def register(request):
     if request.method== 'POST':
         username=request.POST['username']
         password=request.POST['password']
         cpassword=request.POST['password1']
         if password == cpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"user name already taken")
                 return redirect('register')
             # elif User.objects.filter(password=password).exists():
             #     messages.info(request,"password already taken")
             #     return redirect('register')

             else:

               user=User.objects.create_user(username=username,password=password)
               user.save();
               return redirect('login')


         else:
               messages.info(request,"password not matching")
               return redirect('register')



     return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/login/")
def new_uploads(request):

    # if request.method =='FILES':
    #     user_name=User.objects.get(id=1).user.id
        form=updateforms(request.POST,request.FILES)
        if form.is_valid():
         form.save()
         return  redirect("uploads")

        else:



         context={'form':form}
        return render(request,'new_uploads.html',context)
@login_required(login_url="/login/")
def uploads(request):
    File=Upload.objects.all()
    return render(request,'uploads.html',{'files':File})

