from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
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
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Meja di restoran {self.restorant} degan nomor meja {self.no_meja}"

class PenggunaKhusus(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pengguna = models.ForeignKey(PenggunaKhusus, on_delete=models.CASCADE,related_name='reservasi')
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE , related_name='reservasi')
    meja = models.ForeignKey(Meja, on_delete=models.CASCADE,related_name='reservasi')
    tanggal_reservasi = models.DateField()
    waktu_reservasi = models.TimeField()
    jumlah_orang = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Menunggu Konfirmasi', 'Menunggu Konfirmasi'),
        ('Dikonfirmasi', 'Dikonfirmasi'),
        ('Dibatalkan', 'Dibatalkan'),
        ('Selesai', 'Selesai'),
    ])
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Reservasi untuk {self.pengguna} di {self.restoran} pada {self.tanggal_reservasi}"

class Ulasan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pengguna = models.ForeignKey(PenggunaKhusus, on_delete=models.CASCADE, blank=True, null=True,related_name='ulasan')
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE,related_name='ulasan')
    rating = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(6)],)
    komentar = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ulasan untuk {self.pengguna} di {self.restoran}"

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restorant = models.ForeignKey(Restorant, on_delete=models.CASCADE , related_name='daftar_menu')
    menu = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(100000000)])

    def __str__(self):
        return f"{self.restoran} - {self.menu}"
