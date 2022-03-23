from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100,)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='tag', through='TagArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class TagArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,  verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной', blank=True, default=False)

    class Meta:
        verbose_name = 'Тематика Статьи'
        verbose_name_plural = 'Тематика статьи'

