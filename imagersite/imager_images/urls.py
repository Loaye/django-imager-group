"""Imager Images urls."""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from imager_images.views import AlbumView, LibraryView, PhotoView, EditAlbum, EditImage

urlpatterns = [
    url(r'^library/$',
        LibraryView.as_view(template_name='imager_images/library.html'),
        name='library'),
    url(r'^albums/(?P<pk>\d+)/$',
        AlbumView.as_view(template_name='imager_images/album.html'),
        name='album'),
    url(r'^photos/(?P<pk>\d+)/$',
        PhotoView.as_view(template_name='imager_images/photo.html'),
        name='photo'),
    url(r'^albums/(?P<pk>\d+)/edit/$',
        EditAlbum.as_view(template_name='imager_images/edit_album.html'),
        name='edit_album'),
    url(r'^photos/(?P<pk>\d+)/edit/$',
        EditImage.as_view(template_name='imager_images/edit_photo.html'),
        name='edit_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
