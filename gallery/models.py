# -*- coding: utf-8 -*-
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to= 'uploads/gallery', max_length=256, verbose_name=u'картинка')
    date = models.DateField(auto_now_add=True, blank=True, verbose_name=u'дата написания')
    
    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
    
    def __unicode__(self):
        return str(self.id)