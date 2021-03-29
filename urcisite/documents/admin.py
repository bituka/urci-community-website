from django.contrib import admin

# Register your models here.
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_title', 'doc_link')

admin.site.register(Document, DocumentAdmin)