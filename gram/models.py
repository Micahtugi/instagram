from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    location = models.CharField(max_length=100)
    content = models.ImageField(upload_to='timeline_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('gram-home')


class Comment(models.Model):
    post = models.ForeignKey('gram.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
# Create your models here.
