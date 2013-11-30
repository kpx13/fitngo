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

PAGINATION_COUNT = 5

def get_common_context(request):
    form = OrderForm()
    hform = OrderHForm()
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
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, u'Ваша заявка успешно отправлена.')
                form = OrderForm()
            else:
                if request.POST['action'] == 'signup':
                    c['show_signup'] = True
                if request.POST['action'] == 'get':
                    c['show_get'] = True
                messages.error(request, u'Необходимо ввести имя.')

    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['reviews'] = Review.objects.all()[:3]
    c['form'] = form
    c['hform'] = hform
    c['menu'] = Menu.objects.filter(parent=None)
    c['partners'] = Partner.objects.all()
    c['complex'] = Page.get_by_slug('complex').content
    
    try:
        c['menu_cat'] = Menu.get_by_href(request.path).parent
    except:
        c['menu_cat'] = None
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get_by_slug(page_name)
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slider'] = Slider.objects.all()
    c['need_slider'] = len(c['slider']) > 1
    c['c1'] = Page.get_by_slug('home_1').content
    c['c2'] = Page.get_by_slug('home_2').content
    c['c3'] = Page.get_by_slug('home_3').content
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def news(request):
    c = get_common_context(request)
    c['news'] = News.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def programs(request):
    c = get_common_context(request)
    c['news'] = Program.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def reviews(request):
    c = get_common_context(request)
    c['reviews_all'] = Review.objects.all()
    return render_to_response('reviews.html', c, context_instance=RequestContext(request))

def gallery(request):
    c = get_common_context(request)
    c['gallery'] = Photo.objects.all()
    return render_to_response('gallery.html', c, context_instance=RequestContext(request))
