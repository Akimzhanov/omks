# Generated by Django 4.1.4 on 2022-12-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=220, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='smart_images')),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='smartphones.brand')),
            ],
        ),
        migrations.CreateModel(
            name='SmartImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='smart_images/carousel')),
                ('smart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smart_images', to='smartphones.smartphone')),
            ],
        ),
    ]
