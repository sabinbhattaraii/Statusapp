from django.db import models

#from user.model import User
#from django.conf import setting 
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class StatusMessage(models.Model):
    status = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user