# Generated by Django 4.2.7 on 2023-11-14 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='data_received',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='site',
            name='data_sent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='site',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='site',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserStats',
        ),
    ]
