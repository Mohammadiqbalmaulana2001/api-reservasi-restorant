# Generated by Django 5.0.4 on 2024-07-06 02:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_reservasi_meja_alter_reservasi_pengguna_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasi',
            name='pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservasi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ulasan',
            name='pengguna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ulasan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PenggunaKhusus',
        ),
    ]
