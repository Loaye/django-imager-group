"""Views for this awesome app."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
from imager_images.forms import AlbumForm


class UserView(TemplateView):
    """View profile of other users."""

    model = ImagerProfile


class ProfileView(TemplateView):
    """Profile view class based view."""

    model = ImagerProfile


class EditProfileView(CreateView):
    """Edit profile information."""
    model = ImagerProfile
    user_id = ImagerProfile.user_id
    fields = [
        'website',
        'location',
        'bio',
        'camera',
        'services',
        'photo_styles',
        'fee',
        'phone'
    ]
    success_url = reverse_lazy('user_profile')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            self.object = form.save()
            return super(EditProfileView, self).form_valid(form)
        else:
            raise Http404()


class AddImage(CreateView):
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


class AddAlbum(CreateView):
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
