# Generated by Django 3.2.15 on 2022-09-05 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0001_initial'),
        ('Publicity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicity',
            name='service',
            field=models.ManyToManyField(blank=True, through='Publicity.PublicityService', to='Publicity.Service'),
        ),
        migrations.AlterField(
            model_name='publicity',
            name='street',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='Address.street'),
        ),
        migrations.AlterField(
            model_name='publicity',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='Publicity.typepublicity'),
        ),
        migrations.AlterField(
            model_name='publicityservice',
            name='publicity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicity.publicity'),
        ),
        migrations.AlterField(
            model_name='publicityservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Publicity.service'),
        ),
    ]