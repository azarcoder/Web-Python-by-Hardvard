from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
# Create your views here.




tasks = ['make coffee', 'read book', 'make food']

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    return HttpResponse('index of task')

def tas(request):
    return render(request, 'task/tasks.html', {'task' : tasks})


def add(request):
    if request.method == 'POST':
        form = newTaskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data())# it returns a dictionary 
            task = form.cleaned_data["task"]#here task is a variable name inside form
            tasks.append(task)
            return redirect('taskss')
        else:
            return render(request, 'task/add.html', {"form" : newTaskForm()})
    return render(request, 'task/add.h tml', {"form" : newTaskForm()})