# Generated by Django 3.0.8 on 2020-10-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20201026_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ranking',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]