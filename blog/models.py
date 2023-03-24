from django.db import models


# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Date = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='images')


class Meta:
    db_table = "blogs"
