# Generated by Django 5.2 on 2025-04-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactinquiry_sellrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
