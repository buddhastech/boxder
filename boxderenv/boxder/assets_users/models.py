from django.db import models

class Departments(models.Model):

    department_id = models.AutoField(primary_key=True, unique=True, blank=False, 
    null=False, verbose_name="department_id")
    name = models.CharField(max_length=60, blank=False, null=False)
    creation_date = models.DateField(auto_now=True, blank=False, 
    null=False, verbose_name="create_date")
    staff_amount = models.IntegerField(blank=True, null=True, verbose_name="staff_amount")

    class Meta:

        db_table = "departments"


# Create your models here.
class Users(models.Model):
    
    identification_card = models.CharField(primary_key=True, max_length=15, blank=False,
    null=False, unique=True, verbose_name="identification_card")
    name = models.CharField(max_length=255, blank=False, null=False)
    surnames = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=14, blank=False, null=False, unique=True, 
    db_index=True)
    department = models.ForeignKey(Departments, on_delete=models.PROTECT)
    age = models.CharField(max_length=2, blank=False, null=False)
    status = models.BooleanField(default=False)
    admission_date = models.DateField(auto_now=True, verbose_name="admission_date",
    db_index=True)
    administrator = models.BooleanField(default=False, verbose_name="administrator")
    email = models.EmailField(unique=True, blank=False, null=False, db_index=True)
    password = models.CharField(blank=False, null=False, max_length=255)

    class Meta:

        db_table = "users"


class Assets(models.Model):

    code = models.CharField(primary_key=True, max_length=8, blank=False, 
    null=False, unique=True)
    brand = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    name = models.CharField(max_length=255, default="")
    model = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    useful_life = models.IntegerField(blank=True, null=True, verbose_name="useful_life")
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False,
    db_index=True)
    weight = models.IntegerField(blank=True, null=True)
    admission_date = models.DateField(auto_now=True, verbose_name="admission_date",
    blank=False, null=False, db_index=True)

    actual_status = models.CharField(max_length=30,
    verbose_name="actual_status", db_index=True)
    provider = models.CharField(max_length=60, blank=False, null=False, db_index=True)
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id")
    
    class Meta:

        db_table = "assets"


class AccumulatedMoney(models.Model):

    accumulated_id = models.AutoField(primary_key=True, unique=True, verbose_name="accumulated_id")
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id")
    accumulated = models.DecimalField(max_digits=8, decimal_places=6, blank=False, null=False)

    class Meta:

        db_table = "accumulated_money"


class UserSuspensions(models.Model):

    suspension_id = models.AutoField(primary_key=True, unique=True, verbose_name="suspension_id")
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id")
    number_of_suspenssions = models.IntegerField(blank=False, null=False,
    verbose_name="number_of_suspenssions")

    class Meta:

        db_table = "user_suspensions"



class Depreciations(models.Model):

    depreciation_code = models.AutoField(primary_key=True, unique=True, 
    verbose_name="depreciation_code")
    assets_code = models.ForeignKey(Assets, on_delete=models.PROTECT, verbose_name="assets_code")
    depreciation = models.DecimalField(max_digits=8, decimal_places=6, blank=False, null=False,
    db_index=True)

    class Meta:

        db_table = "depreciations"



