from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/upload$', views.upload_project, name='upload'),
<<<<<<< HEAD
    url(r'^myprofile/$',  views.profilemy,name='profilemy'),
=======
    url(r'^new/profile$', views.add_profile, name='addprofile'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
>>>>>>> b4f712487ae02e5ab7e95fbf74ad02442a8c33ba
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)