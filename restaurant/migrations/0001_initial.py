# Generated by Django 4.2.11 on 2024-03-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(default='1', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('no_of_guest', models.IntegerField()),
                ('booking_date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(default='1', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inventory', models.IntegerField()),
            ],
        ),
    ]
