# Generated by Django 3.0.3 on 2020-02-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pno', models.IntegerField()),
                ('pname', models.CharField(max_length=64)),
                ('pruns', models.IntegerField()),
                ('pteam', models.CharField(max_length=64)),
            ],
        ),
    ]
