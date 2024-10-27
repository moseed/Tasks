from django import forms
from tasks.models import Tasks,TaskJob,TaskType

field_attrs = {'class':'form-control mb-2'}

#class TasksForm(forms.Form):
#    Task_Desc = forms.CharField()
#    Task_type = forms.ModelChoiceField(TaskType.objects.all())
#    Task_Job = forms.ModelChoiceField(TaskJob.objects.all())
#    Task_date = forms.DateField(input_formats=['%d/%m/%Y'])
#    #,initial=datetime.date.today

class TasksForm(forms.ModelForm):
    class Meta :
        model = Tasks     
        fields =['comp_id','taskdesc','tasktype','taskjob','taskdate','fromtime','totime','notes']
        widgets = {
            'comp_id': forms.Select(attrs=field_attrs),
            'taskdesc': forms.TextInput(attrs=field_attrs),
            'tasktype': forms.Select(attrs=field_attrs),
            'taskjob': forms.Select(attrs=field_attrs),
            'taskdate': forms.TextInput(attrs=field_attrs),
            'fromtime':forms.TextInput(attrs=field_attrs) ,
            'totime' : forms.TextInput(attrs=field_attrs) ,
            'notes' : forms.Textarea(attrs=field_attrs) 
        }


