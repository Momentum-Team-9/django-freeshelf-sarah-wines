# Generated by Django 3.2.4 on 2021-08-17 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='website',
            new_name='url',
        ),
    ]
