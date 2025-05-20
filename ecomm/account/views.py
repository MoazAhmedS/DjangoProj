from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.views import View
from .forms import  *
from django.shortcuts import render, redirect

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if (form.is_bound):
            obj = authenticate( request,username=request.POST['username'],password= request.POST['password'])
            if (obj is not None):
                login(request,obj)
                return redirect('index')
            else:
                return render(request, '/login.html', {'form': form,'msg':'invlaid username & pass'})
        else:
            return render(request, '/login.html', {'form': form})


class Signup(View):
    def get(self,request):
        return render(request,'register.html',{'form':RegistrationForm()})
    def post(self,request):
        form=RegistrationForm(data=request.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('login')
        else:
            return redirect('register')