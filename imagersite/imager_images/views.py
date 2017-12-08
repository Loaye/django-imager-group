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
  
class EditAlbum(CreateView):
    """View for adding a album."""

    model = Album
    form_class = AlbumForm

    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()
            return super(AddAlbum, self).form_valid(form)
        else:
            raise Http404()

class EditImage(CreateView):
    """View for adding a image."""

    model = Photo
    fields = [
        'image',
        'title',
        'description',
        'published'
    ]
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()
            return super(AddImage, self).form_valid(form)
        else:
            raise Http404()