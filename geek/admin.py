from django.contrib import admin
from .models import Programmers_profile,Project,Chat

# Register your models here.
admin.site.register(Project)
admin.site.register(Programmers_profile)
admin.site.register(Chat)