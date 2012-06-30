#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):


    context = {}

    return render_to_response('home/index.html',
                              context,
                              context_instance=RequestContext(request))



##################################
from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    try:
        return settings.__getattr__(name)
    except AttributeError:
        return ""