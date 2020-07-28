from django.db import models

# Create your models here.

class Users(models.Model):
    
    identification_card = models.CharField(primary_key=True, max_length=15, blank=False,
    null=False, unique=True, verbose_name="identification_card")
    name = models.CharField(max_length=255, blank=False, null=False)
    surnames = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=14, blank=False, null=False, unique=True)
    department = models.CharField(max_length=255, blank=False, null=False)
    age = models.CharField(max_length=2, blank=False, null=False)
    status = models.BooleanField(default=False)
    admission_date = models.DateField(auto_now=True)
    email = models.CharField(max_length=255, unique=True)

    class Meta:

        db_table = "users"

class Assets(models.Model):

    code = models.CharField(primary_key=True, max_length=8, blank=False, 
    null=False, unique=True)
    brand = models.CharField(max_length=255, blank=False, null=False)
    model = models.CharField(max_length=255, blank=False, null=False)
    useful_life = models.IntegerField(max_length=2, blank=False, null=False)
    cost = models.FloatField(max_digits=4,decimal_place=2)
    # max_digits = total de digitos
    #decimal_place = total de decimales
    # 58.979 = max_digits 5 decimal_place = 3