# Generated by Django 3.2 on 2021-10-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdl',
            name='Mob',
            field=models.IntegerField(default=12, max_length=245),
            preserve_default=False,
        ),
    ]
