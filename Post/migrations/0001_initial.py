# Generated by Django 3.2.11 on 2022-02-01 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owners_name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.", regex='^\\+?1?\\d{10}$')])),
                ('location', models.URLField(null=True)),
                ('image1', models.ImageField(default=True, upload_to='images/')),
            ],
        ),
    ]
