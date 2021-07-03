from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Page(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField("date published", auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
