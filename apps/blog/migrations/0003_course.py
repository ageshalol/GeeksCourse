# Generated by Django 4.2.7 on 2023-11-06 20:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('nurchik', '0009_review'),
        ('blog', '0002_blog_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название курса')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='course_image/', verbose_name='Фотография')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('price_min', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена со скидкой')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('teachers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_title', to='nurchik.teachers', verbose_name='Преподователь курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
