# Generated by Django 3.2.8 on 2021-12-26 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0002_auto_20211226_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forlocal.owner'),
        ),
    ]
