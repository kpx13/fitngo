# -*- coding: utf-8 -*-
from django.db import models
import pytils

class Menu(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='submenu', verbose_name=u'родительский пункт меню')
    title = models.CharField(max_length=256, verbose_name=u'заголовок')
    href = models.CharField(max_length=256, blank=True, verbose_name=u'ссылка')
    order = models.IntegerField(blank=True, null=True, verbose_name = u'порядковый номер')
    
    def save(self, *args, **kwargs):
        if not self.href:
            self.href = '/' + pytils.translit.slugify(self.title) + '/'
        super(Menu, self).save(*args, **kwargs)
        if not self.order:
            self.order = self.id
            self.save()
    
    @staticmethod
    def get_by_href(href):
        return Menu.objects.get(href=href)
    
    class Meta:
        verbose_name = u'пункт меню'
        verbose_name_plural = u'меню'
        ordering=['order']
        
    def __unicode__(self):
        return self.title