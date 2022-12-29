from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_values = [form.cleaned_data.get(
            'is_main') for form in self.forms]
        truth = is_main_values.count(True)
        if truth == 0:
            raise ValidationError('Укажите основной раздел')
        elif truth > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
