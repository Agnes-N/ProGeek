from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_content = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save_chat(self):
        self.save()
        
    def delete_chat(self):
        self.delete()    
