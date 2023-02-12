#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "app.api"
urlpatterns = [
    path("", views.IndexView.as_view()),
    path("parlance/", views.ParlanceView.as_view()),
]
