# Generated by Django 4.1.1 on 2022-09-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0008_blog_url_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='2022 Sep 25', max_length=200),
        ),
    ]
