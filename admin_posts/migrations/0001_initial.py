# Generated by Django 4.2.7 on 2024-02-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='admin_posts/media/uploads/')),
                ('book_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('borrow_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('book_category', models.ManyToManyField(blank=True, null=True, to='categories.categorymodel')),
            ],
        ),
    ]