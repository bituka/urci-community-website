from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views import generic


from .models import Announcement


class IndexView(generic.ListView):
    template_name = 'announcement/index.html'
    context_object_name = 'latest_announcement_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Announcement.objects.order_by('-pub_date')[:5]