from django.db.models import manager
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from pages.models import Page
from cs.api.serializers import CommentSerializer
from cs.models import Comment


class PageListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ("name", "url", "id")

    def get_url(self, obj):
        return obj.slug


class PageDetailSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Page
        fields = ("id", "name", "comments")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def get_comments(self, obj):
        comment_qs = Comment.objects.filter(page_id=obj.id)
        comment = CommentSerializer(comment_qs, many=True).data
        return comment
