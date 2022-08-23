# Generated by Django 3.2.15 on 2022-08-20 05:52

import Operation.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Animal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationdate', models.DateField(blank=True)),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(limit_choices_to=Operation.models.limitanimal, on_delete=django.db.models.deletion.PROTECT, to='Animal.animal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('namear', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('vaccinedate', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.vaccinetype')),
            ],
            options={
                'verbose_name_plural': 'Vaccines',
            },
        ),
        migrations.CreateModel(
            name='ReviewOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('descriptionar', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews Operations',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Operation.models.animal_images_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation')),
            ],
            options={
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('certificatedate', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.certificatetype')),
            ],
        ),
    ]
