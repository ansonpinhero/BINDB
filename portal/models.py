from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User



class MalwareFiles(models.Model):
    file_name = models.CharField(max_length=100,default="NONE")
    sha_256 = models.CharField(max_length=100,unique = True)
    file_size = models.IntegerField(blank=True, null=True,default=0)
    timestamp = models.DateField(default=now)

    def __str__(self):
        return self.sha_256


class BenignFiles(models.Model):
    file_name = models.CharField(max_length=100,default="NONE")
    sha_256 = models.CharField(max_length=100,unique = True)
    file_size = models.IntegerField(blank=True, null=True,default=0)
    timestamp = models.DateField(default=now)

    def __str__(self):
        return self.sha_256


