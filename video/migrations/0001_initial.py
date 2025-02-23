# Generated by Django 5.1.4 on 2025-01-08 16:40

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits.', regex='^\\d{10}$')])),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
