from django.db import models

class District(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class Account(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class form_register(models.Model):
    name = models.CharField(max_length = 100)
    DOB = models.DateField()
    AGE = models.CharField(max_length = 2)
    Gender = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 10)
    email_id = models.EmailField()
    address = models.TextField(max_length = 100)
    district = models.ForeignKey(District,on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    account_type = models.ForeignKey(Account,on_delete = models.CASCADE)
    debit_card = models.BooleanField( default = False)
    credit_card = models.BooleanField(default = False)
    Cheque_book = models.BooleanField( default = False)

    def __str__(self):
        return '{}'.format(self.name)