# Generated by Django 3.0.3 on 2020-05-22 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='course',
        ),
    ]
