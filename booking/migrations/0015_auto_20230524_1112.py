# Generated by Django 3.2.18 on 2023-05-24 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20230518_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.capacity'),
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
