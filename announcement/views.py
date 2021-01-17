from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 
from . import forms
from . import models
# Create your views here.

class AnnouncementListView(generic.ListView,LoginRequiredMixin):
    model = models.Announcement

class AnnouncementDetailView(generic.DetailView, LoginRequiredMixin):
    model = models.Announcement

class AnnouncementUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = models.Announcement
    form_class = forms.AnnouncementForm

class AnnouncementCreateView(generic.CreateView, LoginRequiredMixin):
    model = models.Announcement
    form_class = forms.AnnouncementForm

class AnnouncementDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = models.Announcement
    form_class = forms.AnnouncementForm
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


