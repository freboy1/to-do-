from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import TaskModel
from .forms import TaskModelForm

# Create your views here.
def index(request):
    tasks = TaskModel.objects.all()
    form = TaskModelForm()
    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'tasks/index.html', context)

def update(request, id):
    task = TaskModel.objects.get(id=id)

    form = TaskModelForm(instance=task)
    context = {'task': task, 'form': form}

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'tasks/update.html', context)

def delete(request, id):
    task = TaskModel.objects.get(id=id)
    context = {'task': task}

    return render(request, 'tasks/delete.html', context)