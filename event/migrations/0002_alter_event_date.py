# Generated by Django 3.2 on 2022-08-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
