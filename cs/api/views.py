from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from cs.api.serializers import CommentDetailSerializer,CommentEditSerializer, CommentSerializer, create_comment_serializer
from cs.api.pagination import CustomPagination
from cs.models import Comment


class CommentCreateAPIView(CreateAPIView):
    """
    API view to create a coment.
    """

    queryset = Comment.objects.all()

    def get_serializer_class(self):
        page_id = self.request.GET.get("page")
        parent_id = self.request.GET.get("parent")
        return create_comment_serializer(page_id, parent_id)


class CommentListAPIView(ListAPIView):
    """
    API view to get comments in lists view
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(active=True)
    pagination_class = CustomPagination


class CommentDetailAPIView(RetrieveAPIView):
    """
    API view to retrieve comments in detail view
    """

    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.filter(active=True)


class CommentEditAPIView(RetrieveUpdateDestroyAPIView):
    """
    API edit, delete comments
    """

    serializer_class = CommentEditSerializer
    queryset = Comment.objects.filter(active=True, id__gt=0)
