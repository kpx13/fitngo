# -*- coding: utf-8 -*-
from django.db import models

from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template
from django.forms import ModelForm, Form, fields

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])

class Subscribe(models.Model):
    email  = models.CharField(u'Email', max_length=255)
    request_date = models.DateTimeField(u'дата заявки', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'подписка'
        verbose_name_plural = u'подписки'
        ordering = ['-request_date']
        
    def save(self, *args, **kwargs):
        super(Subscribe, self).save(*args, **kwargs)
        subject=u'Новая подписка'
        
        body_templ="""
        Email: {{ form.email }}
            """
        ctx = Context({
            'form': self,

        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)

    def __unicode__(self):
        return self.email
