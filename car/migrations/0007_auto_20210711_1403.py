# Generated by Django 3.2.4 on 2021-07-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20210709_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booked',
            name='owner_phone',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='booked',
            name='renter_phone',
            field=models.CharField(default=None, max_length=10),
        ),
    ]