# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'parent', 'order')

admin.site.register(models.Menu, MenuAdmin)