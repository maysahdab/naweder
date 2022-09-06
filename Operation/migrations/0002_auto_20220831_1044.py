# Generated by Django 3.2.15 on 2022-08-31 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencyapp', '0002_auto_20220820_0852'),
        ('Operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operationtype',
            field=models.CharField(choices=[('Auction', 'Auction'), ('Sale', 'Sale')], default='Auction', max_length=10),
        ),
        migrations.CreateModel(
            name='RefundRequestOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refunddate', models.DateField(verbose_name='Refund Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.operation', verbose_name='Operation Refund')),
            ],
        ),
        migrations.CreateModel(
            name='RefundOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('descriptionar', models.CharField(blank=True, default='', max_length=250, verbose_name='description arabic')),
                ('amount', models.DecimalField(decimal_places=1, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
                ('refund', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Operation.refundrequestoperation')),
            ],
        ),
    ]