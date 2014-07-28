# -*- coding: utf-8 -*-

from django.db import models


class OrderH(models.Model):
    name  = models.CharField(u'Имя', max_length=255)
    phone  = models.CharField(u'Телефон', max_length=255)
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заявка с главной'
        verbose_name_plural = u'заявки с главной'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return self.name

