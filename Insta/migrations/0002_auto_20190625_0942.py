# Generated by Django 2.0 on 2019-06-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ImageField(upload_to='images'),
        ),
    ]