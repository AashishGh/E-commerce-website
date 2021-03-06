# Generated by Django 3.2.11 on 2022-02-02 05:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_rename_owners_name_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 digits and  entered in the format: '98XXXXXXXX'.", regex='^\\+?1?\\d{10}$')])),
                ('image1', models.ImageField(default=True, upload_to='images/')),
                ('selling_price', models.PositiveIntegerField()),
                ('GoogleMap_Location', models.URLField(null=True)),
                ('description', models.TextField()),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
