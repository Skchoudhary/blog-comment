from django.db import models
from pages.models import Page


class Comment(models.Model):
    """
    Comment for pages,..
    """

    #  best will be to a genric FK so that comment can be plugin to any models
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name="page_comments"
    )

    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )

    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return f"Comment on {self.page}"

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
