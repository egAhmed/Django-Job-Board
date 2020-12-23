from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger,  EmptyPage
from .forms import ApplyForm,JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from .filters import JobFilter
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list,9)
    page = request.GET.get('page',1)

    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    context = {
        'jobs':jobs,
        'job_list':job_list
    }
    return render(request,'job/job_list.html',context)


def job_detail(request,slug):
    job = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            print('Done')

    else:
        form = ApplyForm()
    

    context = {
        'job':job,
        'form':form
    }
    return render(request,'job/job_detail.html',context)


@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})
