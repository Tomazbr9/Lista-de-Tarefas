from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import ListForm
from .models import ListModel

def index(request):

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            form = ListForm()
    else:
        form = ListForm()

    context = {
        'title_page': 'home',
        'form': form,
        'tasks': ListModel.objects.all() 
    }
    return render(request, 'index.html', context)

def task_view(request, id):
    task = get_object_or_404(ListModel, pk=id)
    
    context = {
        'task': task,
        'title_page': task.title
    }

    return render(request, 'task.html', context)

def delete(request, id):
    task = get_object_or_404(ListModel, pk=id)

    task.delete()

    return redirect('home:index')

def update(request, id):
    task = get_object_or_404(ListModel, pk=id)

    if request.method == "POST":
        form = ListForm(request.POST, instance=task)

        context = {
            'form': form, 
            'task': task,
            'title_page': task.title
        }

        if form.is_valid():
            form.save()
            return redirect('home:task', id=task.pk)
        
        return render(request, 'update.html', context)
    
    context = {
        'form': ListForm(instance=task),
        'task': task,
        'title_page': task.title
    }

    return render(request, 'update.html', context)

def checkbox_view(request, id):
    task = get_object_or_404(ListModel, pk=id)
    if request.method == "POST":   
        task.show = not task.show
        task.save()
    return redirect('home:index')