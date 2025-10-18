from django.db import models

# Create your models here.

class SanPham(models.Model):
    hinhanh = models.TextField(null=True, blank=True)
    masp = models.CharField(max_length=255)
    tensp = models.CharField(max_length=255)
    mota = models.TextField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    madanhmuc = models.CharField(max_length=255)
    mathuonghieu = models.CharField(max_length=255, null=True, blank=True)
    gioitinh = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.tensp
