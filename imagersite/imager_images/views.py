"""Views module for imager_images."""
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.urls import reverse_lazy
from imager_images.models import Album, Photo
from imager_images.forms import AlbumForm, PhotoForm
from imager_profile.views import AddAlbum, AddImage
from django.http import Http404


class LibraryView(TemplateView):
    """Library view class based view."""

    def get_context_data(self):
        """Get album and photos."""
        user = self.request.user
        return {
            'photos': user.photo.all(),
            'albums': user.album.all(),
        }


class PhotoView(DetailView):
    """Photo view class based view."""

    model = Photo
    template_name = 'imager_images/photo.html'


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
    form_class = PhotoForm

    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()
            return super(AddImage, self).form_valid(form)
        else:
            raise Http404()
