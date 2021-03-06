# Generated by Django 3.1.6 on 2021-03-04 08:52

from django.db import migrations, models
import django.db.models.deletion
import main_restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_restaurant', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=40)),
                ('home', models.CharField(max_length=8)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_message', models.CharField(max_length=400)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('hours_start', models.CharField(max_length=5)),
                ('hours_end', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_restaurant.models.Story.get_file_name)),
                ('story', models.CharField(max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_restaurant.models.Team.get_file_name)),
                ('team_info', models.CharField(max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_restaurant.address')),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_restaurant.phone')),
            ],
        ),
    ]
