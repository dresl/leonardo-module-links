
from django.contrib import admin
from django.conf import settings
from ckeditor.widgets import CKEditorWidget
from .models import Link, LinkCategory, LinkTranslation
from django.db import models

class LinkTranslation_Inline(admin.TabularInline):
    model = LinkTranslation
    max_num = len(settings.LANGUAGES)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class Link_Inline(admin.TabularInline):
    model = Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'web_address', 'category', 'ordering', 'visible']
    list_filter = ['category']
    list_per_page = 50
    inlines = [LinkTranslation_Inline, ]
    search_fields = ['name', 'description']


class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    inlines = [Link_Inline, ]

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory, LinkCategoryAdmin)
