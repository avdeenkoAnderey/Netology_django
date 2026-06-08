# coding=utf-8

from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=255)
    author = models.CharField(u'Автор', max_length=255)
    pub_date = models.DateField(u'Дата публикации')
    

    def __str__(self):
        return self.name + " " + self.author
