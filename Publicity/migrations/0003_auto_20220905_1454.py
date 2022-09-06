# Generated by Django 3.2.15 on 2022-09-05 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencyapp', '0002_auto_20220820_0852'),
        ('Publicity', '0002_auto_20220905_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepublicity',
            name='publicity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Publicity_image', to='Publicity.publicity'),
        ),
        migrations.AlterField(
            model_name='publicity',
            name='currency',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency'),
        ),
        migrations.AlterField(
            model_name='publicity',
            name='published',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
