from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Programmers_profile,Project,Chat
from django.contrib.auth.decorators import login_required
from .forms import ChatForm

# Create your views here.

def welcome(request):
    current_user = request.user
    profiless = Profile.objects.filter(id = current_user.id).first()
    all_projects = Project.get_all_projects()
    chat = Chat.objects.all()
    return render(request, 'welcome.html', {"all_projects": all_projects,"profiless":profiless, "chat":chat})

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

@login_required(login_url='/accounts/login/')
def chat(request):
    current_user = request.user
    profile = profile.objects.all()
    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            chat = form.save(commit = False)
            chat.user = profile
            chat.save()
        return redirect('welcome')
    else:
        form = ChatForm
    return render(request, 'chatform.html',{'form':form, 'profile':profile, 'current_user':current_user})
    
