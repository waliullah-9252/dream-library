# Generated by Django 4.2.7 on 2024-02-14 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_posts', '0005_rename_borrow_price_adminpost_borrowed_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminpost',
            old_name='borrowed_price',
            new_name='borrow_price',
        ),
    ]