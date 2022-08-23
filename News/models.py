from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    titlear = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    descriptionar = models.CharField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"


class ImageNews(models.Model):
    image = models.ImageField()
    publicity = models.ForeignKey(News, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Images News"
