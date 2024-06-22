from django.http import HttpResponse
from django.shortcuts import render
from .models import TaskModel
# Create your views here.
def index(request):
    tasks = TaskModel.objects.all()
    context = {'tasks': tasks}

    return render(request, 'tasks/index.html', context)