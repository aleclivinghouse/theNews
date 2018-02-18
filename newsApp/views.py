# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def the_author(request, id):
    #get all the stories associated with that author
    stories = story.objects.filter(author__id = id)
    a_author = author.objects.get(id = id)
    context = {
    'stories': stories,
    'author': a_author
    }
    return render(request, "authors.html", context)

def the_story(request, id):
    a_story = story.objects.get(id = id)
    context = {
    'story': a_story
    }
    return render(request, "stories.html", context)

def the_category(request, id):
    a_category = category.objects.get(id = id)
    story_ids = [j.id for j in story.objects.filter(category__id = id)]
    authors = author.objects.all()
    for x in authors:
        if x.featured == True:
            featured_author = x
            print featured_author

    featured_id = featured_author.id
    authors_stories = story.objects.filter(author__id = featured_id)[:2]




    promoted = []
    latest = []
    for x in story_ids:
        the_story = story.objects.get(id = x)

        if the_story.promoted == True:
            promoted.append(the_story)

        if the_story.promoted != True:
            latest.append(the_story)

    the_promoted = promoted.reverse()

    promoted_len = len(promoted)
    for y in range(8, promoted_len):
        the_latest = promoted[y]
        latest.append(the_latest)

    page = request.GET.get('page', 1)
    paginator = Paginator(latest, 2)

    try:
        the_latest = paginator.page(page)
    except PageNotAnInteger:
        the_latest = paginator.page(1)
    except EmptyPage:
        the_latest = paginator.page(paginator.num_pages)

    categories = category.objects.all()


    context = {
    'category': a_category,
    "headline": promoted[0],
    'second': promoted[1],
    'third': promoted[2],
    'breaking1': promoted[3],
    'breaking2': promoted[4],
    'breaking3': promoted[5],
    'breaking4': promoted[6],
    'breaking5': promoted[7],
    'latest': the_latest,
    'categories': categories,
    'featured_author':featured_author,
    "authors_stories": authors_stories

    }
    return render(request, "categories.html", context)




# Create your views here.
def home(request):
    headline = story.objects.all().latest('created_at')
    story_ids =[j.id for j in story.objects.all()]
    promoted = []
    latest = []
    authors = author.objects.all()
    for x in authors:
        if x.featured == True:
            featured_author = x
            print featured_author

    featured_id = featured_author.id
    authors_stories = story.objects.filter(author__id = featured_id)[:8]


    for x in story_ids:
        the_story = story.objects.get(id = x)

        if the_story.promoted == True:
            promoted.append(the_story)

        if the_story.promoted != True:
            latest.append(the_story)

    the_promoted = promoted.reverse()



    promoted_len = len(promoted)
    for y in range(8, promoted_len):
        the_latest = promoted[y]

        latest.append(the_latest)

    page = request.GET.get('page', 1)
    paginator = Paginator(latest, 10)

    try:
        the_latest = paginator.page(page)
    except PageNotAnInteger:
        the_latest = paginator.page(1)
    except EmptyPage:
        the_latest = paginator.page(paginator.num_pages)

    categories = category.objects.all()



    template = 'home.html'
    context = {
        "headline": promoted[0],
        'second': promoted[1],
        'third': promoted[2],
        'breaking1': promoted[3],
        'breaking2': promoted[4],
        'breaking3': promoted[5],
        'breaking4': promoted[6],
        'breaking5': promoted[7],
        'latest': the_latest,
        'categories': categories,
        'featured_author': featured_author,
        "authors_stories": authors_stories
        }
    return render(request, template, context)



def post_list(request):
    queryset_list = story.objects.all()

    query = request.POST["q"]
    print query
    # if query:
    objects = queryset_list.filter(
    Q(title__icontains=query) |
    Q(description__icontains=query) |
    Q(author__first_name__icontains=query) |
    Q(author__last_name__icontains=query)
    ).distinct()
    print objects

    context = {
        "object_list": objects,
    }

    return render(request, "searchResults.html", context)
