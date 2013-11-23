# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Program(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'заголовок')
    image = models.ImageField(upload_to= 'uploads/news', max_length=256, verbose_name=u'фото')
    content = RichTextField(blank=True, verbose_name=u'текст в подробнее')
    date = models.DateField(verbose_name=u'дата')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Program, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Program.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'программа'
        verbose_name_plural = u'комплексные программы'
        ordering=['-date']
    
    def __unicode__(self):
        return self.slug