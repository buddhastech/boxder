# Generated by Django 3.0.5 on 2020-09-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_users', '0002_delete_usersassets'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
