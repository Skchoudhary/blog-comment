from typing import no_type_check
from rest_framework import serializers
from django.template.defaultfilters import slugify

from pages.models import Page
from cs.models import Page, Comment


def create_comment_serializer(page_id: int, parent_id: int):
    """ """

    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                "id",
                "page_id",
                "content",
                "created_on",
            ]

        def __init__(self, *args, **kwargs):
            self.page_id = None
            self.parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists():
                    self.parent_id = parent_qs.first().id
            if page_id:
                page_qs = Page.objects.filter(id=page_id)
                if page_qs.exists():
                    self.page_id = page_qs.first().id

            return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def create(self, validated_data):
            content = validated_data.get("content")
            comment = Comment(
                content=content, parent_id=self.parent_id, page_id=self.page_id
            )
            comment.save()

            return comment

    return CommentCreateSerializer


class CommentChildSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), source="parent.id"
    )

    class Meta:
        model = Comment
        fields = ("content", "id", "parent_id")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "content", "parent", "page_id", "created_on")

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


class CommentDetailSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "content", "parent", "replies", "page_id", "created_on")

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


class CommentEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "content")
