from django.shortcuts import render
from django.http import HttpResponse

from mscthesis.forms import AreaForm
from mscthesis.models import Status , Student, Supervisor , Thesis, Area, Submission
# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def search(request):
  #  form = AreaForm()
    datas = Area.objects.all()

    args = {
         'datas': datas
    }
    return render(request, 'search.html', args)