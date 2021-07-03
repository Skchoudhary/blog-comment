from django.urls import path
from cs.api.views import CommentListAPIView, CommentDetailAPIView, CommentCreateAPIView, CommentEditAPIView


urlpatterns = [
    path("", CommentListAPIView.as_view(), name="all"),
    path("<int:pk>", CommentDetailAPIView.as_view(), name="thread"),
    path("create/", CommentCreateAPIView.as_view(), name="create"),
    path("<int:pk>/edit/", CommentEditAPIView.as_view(), name="edit"),
    
]
