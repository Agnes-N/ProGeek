from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Programmers_profile,Project
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.

def welcome(request):
    current_user = request.user
    profiless = Profile.objects.filter(id = current_user.id).first()
    all_projects = Project.get_all_projects()
    return render(request, 'welcome.html', {"all_projects": all_projects,"profiless":profiless})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'upload_project.html', {"form": form})

