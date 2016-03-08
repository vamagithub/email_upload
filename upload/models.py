from django.db import models

# Create your models here.


class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    attach = models.FileField()
    message = models.CharField(max_length=250)


    def __str__(self):
        return self.email


