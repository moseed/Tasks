from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.

class TaskType(models.Model):
    typename = models.CharField(null=True)
    typestatus = models.BooleanField(null=True)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.typename


class TaskJob(models.Model):
    jobname = models.CharField(null=True)
    jobstatus = models.BooleanField(null=True)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jobname



class Company(models.Model):
    comp_name = models.CharField(null=False)
    comp_name_e = models.CharField(null=True)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comp_name 

class Tasks(models.Model):    
    taskdesc = models.CharField(null=False)
    tasktype = models.ForeignKey(TaskType, on_delete=models.PROTECT, null=False)
    taskjob  = models.ForeignKey(TaskJob, on_delete=models.PROTECT, null=False)
    taskdate  = models.DateField(default=timezone.now, null=False) 
    comp_id = models.ForeignKey(Company,on_delete=models.PROTECT,null=False)
    teamviwer = models.CharField(null=True)
    version = models.CharField(null=True)
    fromtime = models.TimeField(null=True)
    totime = models.TimeField(null=True)
    amount = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    notes = models.TextField(null=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    #username = models.ForeignKey(auth_user)


