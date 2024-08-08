from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField(max_length=30)
    address=models.TextField(max_length=30)
    

    class Meta:
        db_table='emp'

    def __str__(self):
        return self.name

from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class Account(models.Model):
    salary=models.IntegerField(max_length=30)
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    
    class Meta:
        db_table='account'

from django import forms

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'