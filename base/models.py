from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200,null=True,unique=True)
    email = models.EmailField()

    avatar = models.ImageField(null=True,default="default.png")
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []


class property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    location = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    type = models.CharField(max_length=20,choices=[('house','house'),('Apartment','Apartment'),('office','office'),('room','room'),])
    status = models.CharField(max_length=200, choices=[('Available for rent','Available for rent'),('Available for Sale','Available for Sale'),])
    image = models.ImageField()




    class Meta:
        verbose_name = ("property")
        verbose_name_plural = ("properties")

    def __str__(self):
        return self.type
    