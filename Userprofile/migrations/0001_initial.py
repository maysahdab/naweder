# Generated by Django 3.2.15 on 2022-08-20 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Address.street')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profile1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
