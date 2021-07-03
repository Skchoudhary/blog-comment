from django.urls import path
from django.urls.conf import include
from pages.api.views import PageListCreateAPIView, PageDetailsAPIView
from rest_framework import routers

urlpatterns = [
    path("", PageListCreateAPIView.as_view(), name="page_list"),
    path("<slug:slug>", PageDetailsAPIView.as_view(), name="page_details"),
]
