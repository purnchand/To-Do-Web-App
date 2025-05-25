from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def todo_list(request):
    tasks = Task.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo_list.html', {'form': form, 'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('todo_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo_list')
