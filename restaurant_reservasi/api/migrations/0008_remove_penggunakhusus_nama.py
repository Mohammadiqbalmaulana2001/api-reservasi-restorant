# Generated by Django 5.0.4 on 2024-05-03 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_penggunakhusus_nama_alter_penggunakhusus_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penggunakhusus',
            name='nama',
        ),
    ]