from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    full_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, verbose_name='email')
    text = models.TextField(max_length=250, verbose_name='Описание')
    starts = models.BooleanField(default=True)
    image = models.ImageField("Изображение", upload_to="photo/")

    def __str__(self):
        return f'Client: {self.user}'
