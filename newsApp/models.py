# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


# Create your models here.
class author(models.Model):
    first_name = models.CharField(max_length=120, default="first name")
    last_name = models.CharField(max_length=120, default="first name")
    featured =  models.BooleanField(blank=True, default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profilePic = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __unicode__(self):
        return self.last_name

class category(models.Model):
    name = models.CharField(max_length=120, default="default text")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name



#promoted is 900X450
#wideImage is 400X200
#tallImage is 400X400
#extrawide is 600x400
#thumbnail is 100x100

class story(models.Model):
    author = models.ForeignKey(author)
    category = models.ForeignKey(category, null=True, blank=True)
    title = models.CharField(max_length=120, default="default text")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    promoted =  models.BooleanField(blank=True, default = True)
    promotedImage = models.ImageField(upload_to=upload_location, null=True, blank=True)
    tallImage = models.ImageField(upload_to=upload_location, null=True, blank=True)


    def __unicode__(self):
        return self.title
