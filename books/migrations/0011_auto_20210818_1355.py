# Generated by Django 3.2.6 on 2021-08-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.Author'),
        ),
    ]
