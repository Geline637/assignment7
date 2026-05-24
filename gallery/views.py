from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm

# Album Views
def album_list(request):
    """View all albums"""
    albums = Album.objects.all()
    return render(request, 'gallery/album_list.html', {'albums': albums})

def album_detail(request, pk):
    """View a specific album and its photos"""
    album = get_object_or_404(Album, pk=pk)
    photos = album.photos.all()
    return render(request, 'gallery/album_detail.html', {'album': album, 'photos': photos})

def album_create(request):
    """Create a new album"""
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            messages.success(request, f'Album "{album.name}" created successfully!')
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'gallery/album_form.html', {'form': form, 'title': 'Create Album'})

def album_update(request, pk):
    """Update an existing album"""
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            messages.success(request, f'Album "{album.name}" updated successfully!')
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'gallery/album_form.html', {'form': form, 'title': 'Update Album', 'album': album})

def album_delete(request, pk):
    """Delete an album"""
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album_name = album.name
        album.delete()
        messages.success(request, f'Album "{album_name}" deleted successfully!')
        return redirect('album_list')
    return render(request, 'gallery/album_confirm_delete.html', {'album': album})

# Photo Views
def photo_upload(request, album_pk):
    """Upload photos to an album"""
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album
            photo.save()
            messages.success(request, f'Photo "{photo.title}" uploaded successfully!')
            return redirect('album_detail', pk=album.pk)
    else:
        form = PhotoForm()
    return render(request, 'gallery/photo_form.html', {'form': form, 'album': album, 'title': 'Upload Photo'})

def photo_detail(request, pk):
    """View a single photo"""
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})

def photo_delete(request, pk):
    """Delete a photo"""
    photo = get_object_or_404(Photo, pk=pk)
    album_pk = photo.album.pk
    if request.method == 'POST':
        photo_title = photo.title
        photo.delete()
        messages.success(request, f'Photo "{photo_title}" deleted successfully!')
        return redirect('album_detail', pk=album_pk)
    return render(request, 'gallery/photo_confirm_delete.html', {'photo': photo})