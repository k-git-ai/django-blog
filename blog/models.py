from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    catagory_choicess = (
        ('Audio', 'Audio'),
        ('video', 'video'),
        ('technology', 'technology'),
        ('science', 'science'),
        ('economy', 'economy'),
    )
    title = models.CharField(max_length=200)
    post_content = models.TextField()
    catagory = models.CharField(max_length=200, choices=catagory_choicess)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
