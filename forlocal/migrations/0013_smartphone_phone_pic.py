# Generated by Django 3.2.8 on 2022-03-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0012_auto_20220320_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='phone_pic',
            field=models.ImageField(blank=True, default='aloki1.PNG', null=True, upload_to=''),
        ),
    ]