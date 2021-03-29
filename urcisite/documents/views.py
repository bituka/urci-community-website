from django.shortcuts import render
from .models import Document
from django.views import generic

# Create your views here.
class DocumentListView(generic.ListView):
    template_name = 'documents/doc_list.html'
    context_object_name = 'document_list'

    def get_queryset(self):
        return Document.objects.all()