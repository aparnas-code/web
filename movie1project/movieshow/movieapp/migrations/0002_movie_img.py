# Generated by Django 3.2.22 on 2023-10-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
