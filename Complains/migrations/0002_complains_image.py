# Generated by Django 3.2.15 on 2022-08-24 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Complains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complains',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
