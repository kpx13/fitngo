# -*- coding: utf-8 -*-

from django.db import models


class OrderF(models.Model):
    name  = models.CharField(u'Имя', max_length=255)
    lname  = models.CharField(u'Фамилия', blank=True, max_length=255)
    phone  = models.CharField(u'Телефон', max_length=255)
    email  = models.CharField(u'Email', blank=True, max_length=255)
    city  = models.CharField(u'Населенный пункт', blank=True, max_length=255)
    comment  = models.CharField(u'Комментарий', blank=True, max_length=255)
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заявка на франчайзинг'
        verbose_name_plural = u'заявки на франчайзинг'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return str(self.name)

