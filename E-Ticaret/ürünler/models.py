from tabnanny import verbose
from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length = 50)

    def __str__(self):
        return self.isim

class Ürün(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete = models.CASCADE, null = True)
    isim = models.CharField(max_length = 50)
    resim = models.FileField(upload_to = 'Ürünler/', verbose_name = 'Ürün resimleri')

    def __str__(self):
        return self.isim
   