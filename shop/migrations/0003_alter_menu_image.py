# Generated by Django 4.1.4 on 2023-06-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
