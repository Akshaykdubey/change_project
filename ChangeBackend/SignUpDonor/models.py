from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=70, primary_key=True)


class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)


class PersonalDetails(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=500)


class CCDetails(models.Model):
    ccNum = models.PositiveIntegerField()
    month = models.DateField()
    cvvNum = models.PositiveIntegerField()


class RoundUpDetails(models.Model):

    zipCode = models.CharField(max_length=250)
