from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    photo = model.ImageField(upload_to='photos/',blank=False)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0,null=True)
    

    
    


# Create your models here.
