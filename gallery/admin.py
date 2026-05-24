from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'photo_count']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {}  # Remove if you had slug field
    
    def photo_count(self, obj):
        return obj.photos.count()
    photo_count.short_description = 'Number of Photos'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'uploaded_at']
    list_filter = ['album', 'uploaded_at']
    search_fields = ['title', 'description']