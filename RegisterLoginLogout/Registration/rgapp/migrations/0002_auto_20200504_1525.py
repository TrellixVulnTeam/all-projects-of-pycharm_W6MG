# Generated by Django 3.0.3 on 2020-05-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
