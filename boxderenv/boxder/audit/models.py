from django.db import models
from django.utils import timezone
from assets_users.models import Users # import of assets_users app
from assets_users.models import Assets

class UserRegistration(models.Model):

    registry_id = models.AutoField(primary_key=True, unique=True, verbose_name="registry_id")
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    creation_date = models.DateField(auto_now=True)
    creation_time = models.TimeField(default=timezone.now)

    class Meta:

        db_table = "user_registration"
        order_with_respect_to = "user_id"


class UserModification(models.Model):

    modification_id = models.AutoField(primary_key=True, unique=True, verbose_name="modification_id")
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id") # id usuario modificado
    modifying_id = models.CharField(max_length=15, blank=False, null=False, verbose_name="modifying_id")
    modification_date = models.DateField(auto_now=True, verbose_name="modification_date")
    modification_time = models.TimeField(timezone.now)
    justification = models.CharField(max_length=255, blank=False, null=False)

    class Meta: 

        db_table = "user_modification"
        order_with_respect_to = "user_id"

class IncomesAndExits(models.Model):

    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id")
    date_admission = models.DateField(auto_now=True, verbose_name="admission_date", blank=False, null=False)
    hour_admission = models.TimeField(timezone.now, blank=False, null=False)
    departure_date = models.DateField(auto_now=True, verbose_name="departure_date", blank=False, null=False)
    departura_hour = models.TimeField(default=timezone.now)

    class Meta:

        db_table = "incomes_and_exits"
        order_with_respect_to = "user_id"


class UnauthorizedIncome(models.Model):

    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id")
    try_date = models.DateField(auto_now=True, blank=False, null=False, verbose_name="try_date")
    try_hour = models.TimeField(default=timezone)

    class Meta:

        db_table = "unauthorized_income"
        order_with_respect_to = "user_id"


class AssetModification(models.Model):
    
    modifying_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="modifying_id")
    asset_id = models.ForeignKey(Assets, on_delete=models.PROTECT, verbose_name="asset_id")
    modification_date = models.DateField(auto_now=True, verbose_name="modification_date")
    modification_time = models.TimeField(timezone.now)
    justification = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        
        db_table = "asset_modification"
        order_with_respect_to = "asset_id"


class AssetSuspenssions(models.Model):

    suspension_id = models.AutoField(primary_key=True, unique=True, blank=False, null=False,
    verbose_name="suspension_id")
    asset_id = models.ForeignKey(Assets, on_delete=models.PROTECT, verbose_name="asset_id")
    number_of_suspenssions = models.IntegerField(blank=False, null=False,
    verbose_name="number_of_suspenssions") 


    class Meta:
        
        db_table = "asset_suspenssions"
        order_with_respect_to = "suspension_id"
