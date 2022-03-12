from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()
    # uploaded_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def find_all():
        return Video.objects.all()


class VideoTag(models.Model):
    tag = models.ForeignKey(Tag, related_name="tag", on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name="video", on_delete=models.CASCADE)
