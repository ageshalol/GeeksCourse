from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.
class Blog(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='blog_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions = RichTextField(
        verbose_name="Описание",
        blank=True,null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True
    )
    def __str__(self):
        return f"{self.title} - {self.created_at}"

        
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
