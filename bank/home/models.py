from django.db import models
from django.urls import reverse


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(blank=True)



    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}'.format(self.name)


class Account(models.Model):
    name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Card(models.Model):
    name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class Form(models.Model):
    name = models.CharField(max_length=250,blank=True)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250,blank=True)
    phone = models.CharField(max_length=250,blank=True)
    mail = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=250,blank=True)
    branch = models.CharField(max_length=250,blank=True)
    account = models.CharField(max_length=250,blank=True)
    materials = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return '{}'.format(self.name)




