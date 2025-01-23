from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from .models import Task

from .forms import AddTask

# Create your views here.
@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(user=request.user)
    
    return render(request, 'home.html', {
        'tasks' : tasks
    })
    
@login_required(login_url='login')
def update_completed(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    
    return redirect('home')

@login_required(login_url='login')
def add_task(request):
    form = AddTask(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save(request.user)
        return redirect('home')
    
    return render(request, 'add-task.html', {
        'form' : form
    })
    
@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if task.user != request.user:
        return redirect('home')
    
    task.delete()
    
    return redirect('home')

@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if task.user != request.user:
        return redirect('home')
    
    form = AddTask(task.get_dict())
    
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            form.update(task)
            return redirect('home')
    
    return render(request, 'edit-task.html', {
        'form' : form
    })
    
@login_required(login_url='login')
def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    
    if task.user != request.user:
        return redirect('home')
    
    return render(request, 'task-detail.html', {
        'task':task
    })