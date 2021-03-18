from django.shortcuts import render, redirect
from .forms import NewjobForm
from .models import Newjob


# Create your views here.
def create(request):
    if request.method == "POST":
        form = NewjobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.newjob')
    return render(request, 'job/create.html')


def read(request):
    jobs = Newjob.objects.all()
    return render(request, 'job/read.html', {'jobs': jobs})


def update(request, job_id):
    job = Newjob.objects.get(id=job_id)
    if request.method == "POST":
        form = NewjobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('read.newjob')
    return render(request, 'job/update.html', {'job': job})


def delete(request, job_id):
    job = Newjob.objects.get(id=job_id)
    job.delete()
    return redirect('read.newjob')
