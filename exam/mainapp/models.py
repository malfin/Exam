from django.db import models


class Group(models.Model):
    number = models.CharField(verbose_name='Номер группы', max_length=32)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
