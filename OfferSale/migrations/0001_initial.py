# Generated by Django 3.2.15 on 2022-08-20 05:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerdate', models.DateField(blank=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation')),
            ],
        ),
        migrations.CreateModel(
            name='OfferStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('namear', models.CharField(default='', max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesdate', models.DateField(blank=True)),
                ('finalprice', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='OfferSale.offersale')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.AddField(
            model_name='offersale',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='OfferSale.offerstatus'),
        ),
    ]