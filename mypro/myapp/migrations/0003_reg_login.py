# Generated by Django 5.1.4 on 2025-01-01 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_login_delete_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=5)),
                ('dob', models.DateField()),
                ('qual', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phno', models.BigIntegerField()),
                ('addr', models.TextField()),
                ('loc', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('pswd', models.CharField(max_length=20)),
                ('utype', models.CharField(max_length=20)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.reg')),
            ],
        ),
    ]
