# Generated by Django 4.2.7 on 2024-02-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_posts', '0003_adminpost_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]