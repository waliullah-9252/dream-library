# Generated by Django 4.2.7 on 2024-02-10 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_alter_useraccount_initial_deposit_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='initial_deposit_amount',
        ),
    ]