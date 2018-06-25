from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=250)
    pwd = models.CharField(max_length=15)

    def __str__(self):
        return self.userName

class UserDetails(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=250)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    ccNum = models.PositiveIntegerField()
    month = models.DateField()
    cvvNum = models.PositiveIntegerField()






