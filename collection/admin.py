from gc import collect
from django.contrib import admin

from .models import collection, creator

# admin.site.register(collection)


@admin.register(collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag_list')
    list_display_links = ('id', 'title')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u",".join(o.name for o in obj.tags.all())


@admin.register(creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'software_list')
    list_display_links = ('id', 'name')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('software')

    def software_list(self, obj):
        return u",".join(o.name for o in obj.software.all())
