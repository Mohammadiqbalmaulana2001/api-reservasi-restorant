from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MaxValueValidator  
import uuid

class Restorant(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=12, validators=[MaxLengthValidator(12)])
    waktu_buka = models.TimeField() 
    waktu_tutup = models.TimeField() 

    def __str__(self):
        return self.nama

class Meja(models.Model):
    restorant = models.ForeignKey(Restorant, related_name='daftar_meja', on_delete=models.CASCADE)
    no_meja = models.IntegerField()
    kapasitas = models.IntegerField(blank=True, null=True)
    tersewa = models.BooleanField(default=False)

    def __str__(self):
        return f"Meja di restoran {self.restorant} degan nomor meja {self.no_meja}"

class PenggunaKhusus(AbstractUser):
    nomor_telepon = models.CharField(max_length=12, validators=[MaxLengthValidator(12)])
    alamat = models.TextField()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='pengguna_khusus_set', 
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='pengguna_khusus_set', 
    )

    def __str__(self):
        return self.username

class Reservasi(models.Model):
    pengguna = models.ForeignKey(PenggunaKhusus, on_delete=models.CASCADE)
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE)
    meja = models.ForeignKey(Meja, on_delete=models.CASCADE)
    tanggal_reservasi = models.DateField()
    waktu_reservasi = models.TimeField()
    jumlah_orang = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Menunggu Konfirmasi', 'Menunggu Konfirmasi'),
        ('Dikonfirmasi', 'Dikonfirmasi'),
        ('Dibatalkan', 'Dibatalkan'),
        ('Selesai', 'Selesai'),
    ])

    def __str__(self):
        return f"Reservasi untuk {self.pengguna} di {self.restoran} pada {self.tanggal_reservasi}"

class Ulasan(models.Model):
    pengguna = models.ForeignKey(PenggunaKhusus, on_delete=models.CASCADE)
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    komentar = models.TextField(blank=True)

    def __str__(self):
        return f"Ulasan untuk {self.pengguna} di {self.restoran}"

class Menu(models.Model):
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE)
    menu = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(100000000)])

    def __str__(self):
        return f"{self.restoran} - {self.menu}"
