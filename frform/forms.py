# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import OrderF
from django.conf import settings
from livesettings import config_value
from django.core.mail import send_mail
from django.template import Context, Template
from django.forms import ModelForm, Form, fields

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        ['ceo@fit-n-go.com', ])

class OrderFForm(ModelForm):
    phone  = fields.CharField(label=u'имя', min_length=10)
    class Meta:
        model = OrderF
        exclude = ('date', )
      
    def save(self, *args, **kwargs):
        super(OrderFForm, self).save(*args, **kwargs)
        subject=u'Новая заявка на фрайчайзинг'
        
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
