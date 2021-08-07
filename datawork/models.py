
from django.db import models

# Create your models here.


class contactForm(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class indexHead(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.TextField(max_length=1000)
    subhead = models.TextField(max_length=1500)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
