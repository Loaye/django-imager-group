"""Views module for imager_images."""
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from imager_images.models import Album, Photo
from imager_images.forms import AlbumForm, PhotoForm


class LibraryView(TemplateView):
    """Library view class based view."""

    def get_context_data(self):
        """Gets album and photos"""
        user = self.request.user
        return {
            'photos': user.photo.all(),
            'albums': user.album.all(),
        }


class PhotoView(ListView):
    """Photo view class based view."""
    import pdb; pdb.set_trace()
    model = Photo
    template_name = 'imager_images/photo.html'

    def get_context_data(self, pk=None):
        """Get context data for view."""
        user = self.request.user
        photo = user.photo.get(id=pk)
        return {'photo': photo}


class AlbumView(ListView):
    """Album view class based view."""

    model = Album
    template_name = 'imager_images/album.html'
    # def get_context_data(self, pk=None):
    #     """Get context data for view."""
    #     album = Album.objects.get(id=pk)
    #     return {'album': album}