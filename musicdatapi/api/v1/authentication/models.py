from django.db import models
from django.urls import reverse
from datetime import datetime 
from django.contrib.auth.models import User


class Authentication(models.Model):


    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #get the url of the object
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
    
    #show title as the obejct
    def __str__(self):
        return str(self.user) 
