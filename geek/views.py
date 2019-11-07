from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Programmers_profile,Project,Chat
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm
from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import Programmers_profile
# from django.http import HttpResponse,Http404,HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your views here.

def welcome(request):
    current_user = request.user
    # profiless = Programmers_profile.objects.filter(id = current_user.id).first()
    all_projects = Project.get_all_projects()

    programmers=Programmers_profile.objects.all()
    current_user=request.user
    myprof=Project.objects.filter(id=current_user.id).first()

    return render(request, 'index.html', {"myprof":myprof,"programmers":programmers,"all_projects": all_projects})

# @login_required(login_url='/accounts/login/')
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


# @login_required(login_url='/accounts/login/')
def profilemy(request,username=None):
    current_user=request.user
    programmers=Programmers_profile.objects.all()
    # pictures=Neighbour.objects.filter(location=current_user)
    # busines=Business.objects.all()
    if not username:
        username=request.user.username
       
        # proc_img=Profile.objects.filter(user=current_user).first()
    return render(request,'profilemy.html',locals(),{"programmers":programmers})
