# Generated by Django 4.1.1 on 2022-09-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(max_length=200),
        ),
    ]
