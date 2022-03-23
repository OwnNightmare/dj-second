from django.contrib import admin

from .models import Article, TagArticle, Tag
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class TagArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        self.forms.clear()
        for form in self.forms:
            main_counter = 0
            if main_counter > 0:
                raise ValidationError('Только одно поле может быть основным')
            if form.cleaned_data.get('is_main'):
                main_counter += 1
                # main_tag_index = self.forms.index(form.cleaned_data)
                # popped = self.forms.pop(main_tag_index)
                # self.forms.insert(0, popped)
        return super().clean()


class TagArticleInline(admin.TabularInline):
    model = TagArticle
    formset = TagArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
