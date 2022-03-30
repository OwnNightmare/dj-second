from django.contrib import admin

from .models import Article, TagArticle, Tag
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class TagArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        form_counter = 0
        main_counter = 0
        for form in self.forms:
            if len(form.cleaned_data) > 0:
                if form_counter == 0:
                    if form.cleaned_data.get('is_main') is False:
                        raise ValidationError('Первым выберите основной тэг')
                    else:
                        main_counter += 1
            if main_counter > 1:
                raise ValidationError('Только одно поле может быть основным')
            form_counter += 1
        return super().clean()


class TagArticleInline(admin.TabularInline):
    model = TagArticle
    formset = TagArticleInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
