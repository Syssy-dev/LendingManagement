# Generated by Django 5.1.1 on 2024-09-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lending',
            name='date_due',
            field=models.DateTimeField(default=None),
        ),
    ]
