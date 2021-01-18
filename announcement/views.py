from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse 
from django.contrib import messages
from . import forms
from . import models
# Create your views here.

class AnnouncementListView(LoginRequiredMixin, generic.ListView):
    model = models.Announcement

class AnnouncementDetailView(LoginRequiredMixin, generic.DetailView ):
    model = models.Announcement

    def get_absolute_url(self):
        return reverse('announcement:single', kwargs={'pk': self.pk})
class AnnouncementUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Announcement
    form_class = forms.AnnouncementForm

class AnnouncementCreateView(LoginRequiredMixin, generic.CreateView ):
    model = models.Announcement
    form_class = forms.AnnouncementForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AnnouncementDeleteView(LoginRequiredMixin, generic.DeleteView ):
    model = models.Announcement
    
    def get_success_url(self):
        return reverse('home')

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)


