# Generated by Django 3.2.15 on 2022-08-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complains', '0002_complains_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complains',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imagecomplains',
            name='image',
        ),
        migrations.AddField(
            model_name='imagecomplains',
            name='imageText',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
