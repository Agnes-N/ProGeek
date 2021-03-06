from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Programmers_profile(models.Model):
    names = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True)
    github_link = models.CharField(max_length =30)
    bio = models.CharField(max_length = 300, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    degree= models.CharField(max_length =30)

    @classmethod
    def get_all_programmers(cls):
        instagram_users = cls.objects.all()
        return instagram_users

    def save_programmer(self):
        self.save()

    def delete_programmer(self):
        self.delete()

    @classmethod
    def update_programmer(cls,id,value):
        cls.objects.filter(id = id).update(user_id = new_user)

    @classmethod
    def search_by_programmer(cls,names):
        certain_user = cls.objects.filter(user__names__icontains = names)
        return certain_user

    def __str__(self):
        return self.user


class Project(models.Model):
    title = models.CharField(max_length =30)
    project_image = models.ImageField(upload_to = 'project_images/', null=True)
    description = models.CharField(max_length =300)
    link = models.URLField(max_length=128, db_index=True, unique=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    programmers = models.ForeignKey(Programmers_profile,on_delete=models.CASCADE, null=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    @classmethod
    def get_all_projects(cls):
        all_projects = cls.objects.all()
        return all_projects

    def save_projects(self):
        self.save()

    def delete_projects(self):
        self.delete()
        
    def __str__(self):
        return self.title


class Chat(models.Model):
    chat_content = models.CharField(max_length = 120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def save_chat(self):
        self.save()
    def delete_chat(self):
        self.delete()
    def __str__(self):
        return self.user

# class Partner(models.Model):
#     partner_names = models.CharField(max_length = 60)
#     business_name = models.CharField(max_length = 30)
#     location = models.CharField(max_length = 30)
#     phone = models.IntegerField(default = 0)
#     email = models.EmailField(null= True, unique= True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     partner_profile = models.ForeignKey(Programmers_profile,on_delete=models.CASCADE,null=True)

#     def save_partner(self):
#         self.save()

#     def delete_partner(self):
#         self.delete()
        
#     def __str__(self):
#         return self.partner_names
