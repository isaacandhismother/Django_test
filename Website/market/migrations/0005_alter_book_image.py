# Generated by Django 5.0.4 on 2024-04-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='static/market/images', verbose_name='Load image'),
        ),
    ]
