# Generated by Django 3.1.6 on 2021-02-19 11:39

from django.db import migrations, models
import main_restaurant.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('photo', models.ImageField(upload_to=main_restaurant.models.Category.get_file_name)),
                ('category_order', models.IntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
