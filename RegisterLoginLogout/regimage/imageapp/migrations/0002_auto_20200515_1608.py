# Generated by Django 3.0.3 on 2020-05-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(upload_to=None),
        ),
    ]
