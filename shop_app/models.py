from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name = 'Название')
    parent = models.ForeignKey('self', on_delete = models.PROTECT, null = True, blank = True, related_name='children')
    discription = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        if not self.parent:
            return f'{self.name}'
        return f'{self.parent} -- {self.name}'