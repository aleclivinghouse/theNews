# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class authorAdmin(admin.ModelAdmin):
    class Meta:
        model = author
admin.site.register(author, authorAdmin)


class storyAdmin(admin.ModelAdmin):
    class Meta:
        model = story
admin.site.register(story, storyAdmin)

class categoryAdmin(admin.ModelAdmin):
    class Meta:
        model = category
admin.site.register(category, categoryAdmin)
