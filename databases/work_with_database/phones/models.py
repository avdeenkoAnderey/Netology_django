from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField(verbose_name='Ссылка на изображение')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=False, verbose_name='Поддержка LTE')
    slug = models.SlugField(unique=True, verbose_name='URL-идентификатор')

    def save(self, *args, **kwargs):
        if not self.slug:
            # Заменяем пробелы на дефисы и применяем slugify
            self.slug = slugify(self.name.replace(' ', '-'))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
