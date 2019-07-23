from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth import login ,authenticate ,logout

from mscthesis.forms import AreaForm , SignUpForm , UserLoginForm
from mscthesis.models import Status , Student, Supervisor , Thesis, Area, Submission
# Create your views here.
def index(request):
    return HttpResponse('Hello World')

# def search(request):
#     form = AreaForm()
#     datas = Area.objects.all()

#     args = {
#          'datas': datas
#     }
#     return render(request, 'search.html', args)

class SearchView(TemplateView):
    template_name = 'search.html'

    def get(self, request):
        form = AreaForm()
        areas = Area.objects.all()
        args = {
            'form': form, 'areas':areas
        }
        return render(request, self.template_name, args)


def login_view(request):
    next = request.GET.get('next')  
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username , password = password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form':form,
    }
    return render(request,"authentication/login.html",context)

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    form = SignUpForm(request.POST)
    if request.method =='POST':  
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login(request , user)
            return redirect('/')
        else:
            form = SignUpForm()

    context = {
        'form':form,
    }
    return render(request,'authentication/signup.html',context)