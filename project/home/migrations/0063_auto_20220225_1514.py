# Generated by Django 3.0.9 on 2022-02-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_auto_20220222_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecodespeaker',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
