from django.db import models

# Create your models here.

class job(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add= True)
        
    def __str__(self):
        return self.title
