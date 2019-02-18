from django.db import models

class contact_us(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name+" : "+str(self.mobile)
