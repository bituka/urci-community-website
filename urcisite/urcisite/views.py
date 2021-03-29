
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views import generic
from django.views.generic.list import ListView

from announcement.models import Announcement

class AnnouncementListView(generic.ListView):
    template_name = 'urcisite/index.html'
    context_object_name = 'latest_announcement_list'

    def get_queryset(self):

        return Announcement.objects.order_by('-pub_date')[:5]