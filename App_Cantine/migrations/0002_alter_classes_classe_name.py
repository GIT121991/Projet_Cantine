# Generated by Django 4.2.4 on 2023-10-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Cantine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='classe_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]