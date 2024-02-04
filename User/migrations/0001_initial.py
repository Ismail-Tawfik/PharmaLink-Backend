# Generated by Django 4.2b1 on 2024-02-01 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=8), django.core.validators.RegexValidator(message='Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$')])),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('chronic_disease', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
