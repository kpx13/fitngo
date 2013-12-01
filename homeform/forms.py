# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import OrderH
from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template
from django.forms import ModelForm, Form, fields

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        [config_value('MyApp', 'EMAIL')])

class OrderHForm(ModelForm):
    phone  = fields.CharField(label=u'имя', min_length=7)
    class Meta:
        model = OrderH
        exclude = ('date', )
      
    def save(self, *args, **kwargs):
        super(OrderHForm, self).save(*args, **kwargs)
        subject=u'Кто-то заполнил форму с главной'
        
        body_templ="""
{% for field in form %}
   {{ field.label }} - {{ field.value }}
{% endfor %}
            """
        ctx = Context({
            'form': self,

        })
        body = Template(body_templ).render(ctx)
        sendmail(subject, body)
