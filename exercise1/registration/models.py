from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, validate_email
# Create your models here.

class user_registration(models.Model):
    """docstring foruser_registration."""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    mobile = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(9999999999)])
    email = models.CharField(max_length=35, unique=True, validators=[validate_email])
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username+" : "+self.password

class user_login(models.Model):
    """docstring for user_login."""
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=35, unique=True, validators=[validate_email])
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username+" : "+self.email
