# Generated by Django 5.0.4 on 2024-05-01 23:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_reservasi_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restorant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daftar_menu', to='api.restorant'),
        ),
        migrations.AlterField(
            model_name='reservasi',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ulasan',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ulasan',
            name='komentar',
            field=models.TextField(blank=True, null=True),
        ),
    ]
