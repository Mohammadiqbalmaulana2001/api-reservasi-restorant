from django.db import models

class Restorant(models.Model):
  nama = models.CharField(max_length=100)
  alamat = models.CharField(max_length=255)
  no_telp = models.CharField(max_length=12)
  waktu_Buka = models.TimeField()
  Waktu_Tutup = models.TimeField()

  def __str__(self):
    return self.nama