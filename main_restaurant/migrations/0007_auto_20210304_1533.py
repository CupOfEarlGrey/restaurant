# Generated by Django 3.1.6 on 2021-03-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_restaurant', '0006_auto_20210304_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_email',
            field=models.CharField(max_length=100),
        ),
    ]
