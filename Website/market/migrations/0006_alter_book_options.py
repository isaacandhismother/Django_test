# Generated by Django 5.0.4 on 2024-04-11 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
