from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=250)
    pwd = models.CharField(max_length=15)


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ccNum = models.CharField(max_length=20)