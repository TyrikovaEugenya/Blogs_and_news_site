
from django.db import models

class Articles(models.Model):
    title = models.CharField('Name of article', max_length=50, default='Some article')
    anons = models.CharField('Anons of article', max_length=250, default='Anons')
    full_text = models.TextField('Full text of article')
    date = models.DateTimeField('Time of publication')
    objects = models.Manager() ## Для получения объектов

    def __str__(self):
        return  f'New: {self.title}' ## Можно сделать форматированный вывод

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
