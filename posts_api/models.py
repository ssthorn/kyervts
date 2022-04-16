from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32, default="default")
    description = models.CharField(max_length=32, default="default")
    votesYes = models.IntegerField()
    votesNo = models.IntegerField()
    # slug = models.SlugField(max_length=250, default='published')