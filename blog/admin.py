from django.contrib import admin

from blog import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author', 'published_at', 'is_published')
    list_display_links = ('title', 'slug')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related('category')
        )


