# Generated by Django 3.2.18 on 2023-04-23 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=50)),
                ('user_username', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('user_password', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
    ]