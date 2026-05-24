from django.db import models
from django.urls import reverse

# Try to import CloudinaryField
try:
    from cloudinary.models import CloudinaryField
    CLOUDINARY_AVAILABLE = True
except ImportError:
    CLOUDINARY_AVAILABLE = False
    class CloudinaryField:
        def __init__(self, *args, **kwargs):
            pass

class Album(models.Model):
    """Album model to group photos"""
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    
    # FIXED: Use CloudinaryField for cover photo too
    if CLOUDINARY_AVAILABLE:
        cover_photo = CloudinaryField('cover_photo', blank=True, null=True)
    else:
        cover_photo = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('album_detail', args=[str(self.id)])
    
    def photo_count(self):
        return self.photos.count()

class Photo(models.Model):
    """Photo model for individual photos within albums"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    if CLOUDINARY_AVAILABLE:
        image = CloudinaryField('image')
    else:
        image = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.title} - {self.album.name}"