from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from pages.api.serializers import PageListSerializer, PageDetailSerializer
from pages.models import Page


class PageListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of pages
    """

    serializer_class = PageListSerializer
    queryset = Page.objects.all()


class PageDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete page
    """

    serializer_class = PageDetailSerializer
    queryset = Page.objects.all()
    lookup_field = "slug"
