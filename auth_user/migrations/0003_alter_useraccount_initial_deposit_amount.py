# Generated by Django 4.2.7 on 2024-02-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_alter_useraddress_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='initial_deposit_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
