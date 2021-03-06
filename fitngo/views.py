# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
 

from pages.models import Page
from news.models import Article as News
from programs.models import Program
from order.forms import OrderForm
from order.models import Order
from homeform.forms import OrderHForm
from frform.forms import OrderFForm
from menu.models import Menu
from partners.models import Partner
from subscribe.models import Subscribe
from gallery.models import Photo
from review.models import Review
from slideshow.models import Slider
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import config
from livesettings import config_value
from django.conf import settings
import datetime

PAGINATION_COUNT = 5

def get_common_context(request):
    form = OrderForm()
    hform = OrderHForm()
    fform = OrderFForm()
    c = {}
    if request.method == 'POST':
        if request.POST['action'] == 'subscribe':
            em = request.POST.get('email', None)
            if em:
                Subscribe(email=em).save()
                messages.success(request, u'Вы успешно подписались на рассылку.')
            else:
                messages.error(request, u'Необходимо ввести емейл.')
        elif request.POST['action'] == 'homeform':
            hform = OrderHForm(request.POST)
            if hform.is_valid():
                hform.save()
                messages.success(request, u'Ваша заявка успешно отправлена.')
                hform = OrderHForm()
            else:
                c['show_hform'] = True
                messages.error(request, u'Необходимо ввести имя и телефон.')
        elif request.POST['action'] == 'franchajzing':
            fform = OrderFForm(request.POST)
            if fform.is_valid():
                fform.save()
                messages.success(request, u'Ваша заявка успешно отправлена.')
                fform = OrderFForm()
            else:
                print fform.errors
                c['show_fform'] = True
                messages.error(request, u'Необходимо ввести имя и телефон.')
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                c['request-ok'] = True
            else:
                if request.POST['action'] == 'signup':
                    c['show_signup'] = True
                if request.POST['action'] == 'get':
                    c['show_get'] = True
                if request.POST['action'] == 'gift':
                    c['show_gift'] = True
                messages.error(request, u'Необходимо ввести имя.')

    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['reviews'] = Review.objects.all()[:3]
    c['form'] = form
    c['hform'] = hform
    c['fform'] = fform
    c['menu'] = Menu.objects.filter(parent=None)
    c['partners'] = Partner.objects.all()
    c['complex'] = Page.get_by_slug('complex').content
    
    try:
        c['menu_cat'] = Menu.get_by_href(request.path).parent
    except:
        c['menu_cat'] = None
        
    c['siteurl'] = request.get_host().split('.')[0]
    c['phone'] = config_value('MyApp', 'PHONE')
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    p = Page.get_by_slug(page_name)
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    c['request_url'] = 'home'
    c['slider'] = Slider.objects.all()
    c['need_slider'] = len(c['slider']) > 1
    c['c1'] = Page.get_by_slug('home_1').content
    c['c2'] = Page.get_by_slug('home_2').content
    c['c3'] = Page.get_by_slug('home_3').content
    if datetime.datetime.now().day % 2:
        c['action_name'] = u'+ 1 тренировка в подарок'
    else:
        c['action_name'] = u'Диагностика Состава Тела в Подарок'
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def news(request):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    c['news'] = News.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def programs(request):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    c['news'] = Program.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def reviews(request):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    c['reviews_all'] = Review.objects.all()
    return render_to_response('reviews.html', c, context_instance=RequestContext(request))

def gallery(request):
    c = get_common_context(request)
    if 'request-ok' in c:
        return HttpResponseRedirect('/request-ok/')
    c['gallery'] = Photo.objects.all()
    return render_to_response('gallery.html', c, context_instance=RequestContext(request))
