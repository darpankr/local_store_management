# Generated by Django 3.2.8 on 2022-03-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0013_smartphone_phone_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='rom',
            field=models.CharField(choices=[('2GB', '2GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB')], max_length=100, null=True),
        ),
    ]