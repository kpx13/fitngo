# -*- coding: utf-8 -*-
from django.db import models
from pytils import dt, translit

class Review(models.Model):
    name  = models.CharField(u'имена', max_length=255)
    age  = models.CharField(u'возраст', max_length=255)
    text = models.TextField(u'текст')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['-request_date']

    def __unicode__(self):
        return self.name
