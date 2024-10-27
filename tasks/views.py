
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from tasks.models import TaskType,TaskJob,Tasks
from django.views.generic import ListView, DetailView, FormView, CreateView,UpdateView
from tasks.forms import   TasksForm
from django import forms
# Create your views here.

def indextask(request):
   return render (request,'task/indextask.html')

def maintask(request):
   return render (request='task/maintask.html')

def showtasks(request, id):
    models = Tasks.objects.get(pk=id)
    #models = Tasks.objects.filter(pk=id).first()
    return render(request, 'task/showtask.html',
                  {
                      'task': models
                  })
 
#def create_task(request):
#    if request.method == "POST":
#        form = TasksForm(request.POST)
#        if form.is_valid():
#            task_desc = form.cleaned_data['task_desc']
#            task_type = form.cleaned_data['task_type']
#            task_job = form.cleaned_data['task_job']
#            task_date = form.cleaned_data ['task_date']
#            currencies =  Tasks.objects.create(taskdesc=task_desc,tasktype=task_type,taskdate=task_date)
#            return redirect('/createtask')
#    else:
#        form = TasksForm()
#        return render(request, 'tasks/createtask.html',{
#            'form': form
#    })

class TaskTypeList(ListView):
   model = TaskType 
   template_name = 'task/tasktype.html' 

class TaskJobList(ListView):
   model = TaskJob  
   template_name = 'task/taskjob.html'

class TasksListview(ListView):
   model = Tasks  
   template_name = 'task/tasks.html'
   queryset = Tasks.objects.select_related('tasktype','taskjob')

class TaskDetialview(DetailView):
   model = Tasks
   template_name = 'task/showtasklist.html'
   queryset = Tasks.objects.select_related('tasktype','taskjob')


#class TaskCreateview(FormView):
#   form_class = TasksForm
#   template_name='task/task_create.html'
#   #success_url = '/tasks/'

#def get_success_url(self):
#      return reverse('tasks')


class TaskCreateview(CreateView):
   model = Tasks
   form_class = TasksForm 
   template_name='task/task_create.html'
   success_url = reverse_lazy('tasks')

   def get_form(self, form_class=None):
        form = super().get_form(form_class)
        #form.fields['taskdate'].widget = forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/yyyy'})
        form.fields['taskdate'].input_formats = ['%d/%m/%Y']
        return form
   #def get_success_url(self):
      #return reverse('/')


class TaskUpdateview(UpdateView):
   model = Tasks
   form_class = TasksForm 
   template_name='task/task_update.html'
   success_url = reverse_lazy('tasks')
