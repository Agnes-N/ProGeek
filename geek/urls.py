from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^welcome$',views.welcome,name = 'welcome'),
    url(r'^new/upload$', views.upload_project, name='upload'),
    url(r'^new/profile$', views.add_profile, name='addprofile'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    # url(r'^partner$', views.partners, name='partner'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)