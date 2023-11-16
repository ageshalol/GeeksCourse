from django.db import models
from django_resized.forms import ResizedImageField 

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to='logo_image/',
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на инст",
        blank=True,null=True
    )
    youtube = models.URLField(
        verbose_name="Ссылка на ютуб",
        blank=True,null=True
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank=True,null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройка"
        
class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide_image/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Введите название"
    )
    descriptions = models.TextField(
        verbose_name="Введите описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайд"
        
class About(models.Model):
    image = models.ImageField(
        upload_to="slide_image/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Введите название"
    )
    descriptions = models.TextField(
        verbose_name="Введите описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Team(models.Model):
    image = models.ImageField(
        upload_to="slide_image/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Введите название"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Работа"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"

class Teachers(models.Model):
    image = models.ImageField(
        upload_to="slide_image/",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Введите название"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Работа"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на инст",
        blank=True,null=True
    )
    telegram = models.URLField(
        verbose_name="Ссылка на Telegram",
        blank=True,null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Наши преподователи"
        verbose_name_plural = "Наша преподователи"
        
class Review(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name="Фио"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Специальность"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Наш отзыв"
        verbose_name_plural = "Наши отзывы"
        
class Gallery(models.Model):
    image =  ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='course_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        