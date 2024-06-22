from django.http import HttpResponse
from django.shortcuts import render
from .models import TaskModel
from .forms import TaskModelForm

# Create your views here.
def index(request):
    tasks = TaskModel.objects.all()
    form = TaskModelForm()
    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/index.html', context)

def update(request, id):
    task = TaskModel.objects.get(id=id)
    context = {'task': task}

    return render(request, 'tasks/update.html', context)