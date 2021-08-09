from django.db import models

class Task(models.Model):
    title = models.CharField('Nom', max_length=50)
    task = models.TextField('Tavsif')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topshiriq'
        verbose_name_plural = 'Topshiriqlar'