# Generated by Django 4.1.1 on 2022-09-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0004_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=200000),
        ),
    ]
