from django.shortcuts import render
from .models import *
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    context = {
        'jobs':jobs
    }
    return render(request,'job/job_list.html',context)


def job_detail(request,id):
    job = Job.objects.get(id=id)
    context = {
        'job':job
    }
    return render(request,'job/job_detail.html',context)
