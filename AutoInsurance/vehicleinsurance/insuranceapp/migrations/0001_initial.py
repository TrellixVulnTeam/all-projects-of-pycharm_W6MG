# Generated by Django 3.0.3 on 2020-12-10 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('min_pay', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage_name', models.CharField(max_length=100)),
                ('coverage_group', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_num', models.CharField(max_length=10, unique=True)),
                ('policy_effect_dt', models.DateTimeField()),
                ('policy_expiry_dt', models.DateTimeField()),
                ('payment_option', models.CharField(max_length=100)),
                ('total_amount', models.BigIntegerField()),
                ('active', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('model', models.CharField(max_length=50)),
                ('vehicle_num', models.CharField(max_length=50)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceapp.Policy')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyEditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edited_by', models.CharField(max_length=100)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceapp.Policy')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_dt', models.DateField()),
                ('amount', models.IntegerField()),
                ('pay_method', models.CharField(max_length=25)),
                ('p_first_name', models.CharField(max_length=50)),
                ('p_last_name', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('card_type', models.CharField(max_length=25)),
                ('debit_credit', models.CharField(max_length=25)),
                ('bank_name', models.CharField(max_length=50)),
                ('account_number', models.IntegerField()),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceapp.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceapp.Policy')),
            ],
        ),
    ]
