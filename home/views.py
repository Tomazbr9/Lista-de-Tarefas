from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ListForm, RegisterForm
from .models import ListModel


@login_required(login_url="home:login")
def index(request):

    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            form = ListForm()
    else:
        form = ListForm()

    context = {
        'title_page': 'home',
        'form': form,
        'tasks': ListModel.objects.filter(user=request.user) 
    }
    return render(request, 'index.html', context)

def task_view(request, id):
    task = get_object_or_404(ListModel, pk=id)
    
    context = {
        'task': task,
        'title_page': task.title
    }

    return render(request, 'task.html', context)

@login_required(login_url="home:login")
def delete(request, id):
    task = get_object_or_404(ListModel, pk=id)

    task.delete()

    return redirect('home:index')

@login_required(login_url="home:login")
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

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("home:login")
    else:
        form = RegisterForm()
    
    context = {
        "form": form,
        "title_page": "Register"
    }

    return render(request, "register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home:index")
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
        'title_page': "Login"
    }
    
    return render(request, "login.html", context)


@login_required(login_url="home:login")
def logout_view(request):
    logout(request)
    return redirect("home:index")
