from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Programmers_profile,Project,Chat
from django.contrib.auth.decorators import login_required


def welcome(request):
    current_user = request.user
    profiless = Programmers_profile.objects.filter(id = current_user.id).first()
    all_projects = Project.get_all_projects()
    return render(request, 'index.html', {"all_projects": all_projects,"profiless":profiless})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'upload_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Programmers_profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'add_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    # my_projects = Project.objects.filter(user = current_user)
    my_profile = Programmers_profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"my_profile":my_profile})

    # my_projects = Project.objects.filter(user = current_user)