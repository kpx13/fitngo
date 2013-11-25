# -*- coding: utf-8 -*-
from django.db import models
import pytils

class Partner(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name=u'название')
    url = models.CharField(max_length=200, blank=True, verbose_name=u'url сайта')
    logo = models.ImageField(upload_to=lambda instance, filename: 'uploads/partners/' + pytils.translit.translify(filename),
	max_length=256, verbose_name=u'лого')
        
    class Meta:
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        ordering=['id']
        
    def __unicode__(self):
        return str(self.id)
    
