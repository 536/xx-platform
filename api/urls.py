#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.Index.as_view()),
]
