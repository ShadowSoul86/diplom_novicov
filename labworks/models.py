from django.db import models
from django.utils.text import slugify


class LabWork(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField(default='')
    image1 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image2 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image3 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image4 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image5 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image6 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image7 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image8 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image9 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)
    image10 = models.FileField(
        upload_to='labwork_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def images(self):
        return [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6, self.image7, self.image8, self.image9, self.image10]
