# Generated by Django 3.2.15 on 2022-09-05 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='family',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='user',
        ),
        migrations.AddField(
            model_name='animal',
            name='animalclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Animal.animalclass'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='namear',
            field=models.CharField(max_length=50, verbose_name='name arabic'),
        ),
        migrations.AlterField(
            model_name='animalclass',
            name='descriptionar',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='description arabic'),
        ),
        migrations.AlterField(
            model_name='animalclass',
            name='namear',
            field=models.CharField(max_length=50, verbose_name='name arabic'),
        ),
        migrations.AlterField(
            model_name='animals',
            name='animalclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Animal.animalclass', verbose_name='class animal'),
        ),
        migrations.AlterField(
            model_name='animals',
            name='descriptionar',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='description arabic'),
        ),
        migrations.AlterField(
            model_name='animals',
            name='namear',
            field=models.CharField(max_length=50, verbose_name='name arabic'),
        ),
        migrations.AlterField(
            model_name='family',
            name='descriptionar',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='description arabic'),
        ),
        migrations.AlterField(
            model_name='family',
            name='namear',
            field=models.CharField(max_length=50, verbose_name='description arabic'),
        ),
    ]