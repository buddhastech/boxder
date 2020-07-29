from django.db import models
from assets_users.models import Users

class Reports(models.Model):

    report_id = models.AutoField(primary_key=True, unique=True,
    null=False, blank=False, verbose_name="report_id")
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name="user_id",
    db_index=True)
    creation_date = models.DateField(auto_now=True, blank=False, null=False,
    verbose_name="creation_date", db_index=True)
    affair = models.CharField(max_length=255, blank=False, null=False)
    desciption = models.CharField(max_length=255, blank=False, null=False)
    receiving_mail = models.EmailField()
    status = models.BooleanField(default=False)

    class Meta:

        db_table = "reports"
        order_with_respect_to = "report_id"