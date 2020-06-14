# Generated by Django 3.0.7 on 2020-06-14 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('identifier', models.CharField(blank=True, default=menu.models.hex_uuid, max_length=40)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('price', models.IntegerField(null=True)),
                ('topping', models.CharField(blank=True, max_length=20)),
                ('sauce', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Cart')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Pizza')),
            ],
        ),
    ]
