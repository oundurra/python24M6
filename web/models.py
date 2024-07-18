from django.db import models

# Create your models here.

class Contact(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

class Flan(models.Model):
    flan_id = models.AutoField(primary_key=True)
    flan_name = models.CharField(max_length=64)
    flan_description = models.TextField()
    flan_image_url = models.URLField()
    flan_slug = models.SlugField(default="", blank=True)
    flan_is_private = models.BooleanField()
