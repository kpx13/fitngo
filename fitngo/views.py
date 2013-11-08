# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
 

from pages.models import Page
from news.models import Article as News
from order.forms import OrderForm
from order.models import Order
from gallery.models import Photo
from review.models import Review
from slideshow.models import Slider
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import config
from livesettings import config_value
from django.conf import settings

PAGINATION_COUNT = 5

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['reviews'] = Review.objects.all()
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
    c['content'] = Page.get_by_slug('home').content
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def news(request):
    c = get_common_context(request)
    c['news'] = News.objects.all()
    return render_to_response('news.html', c, context_instance=RequestContext(request))

def gallery(request):
    c = get_common_context(request)
    return render_to_response('gallery.html', c, context_instance=RequestContext(request))
