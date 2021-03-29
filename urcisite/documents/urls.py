from . import views
from django.urls import path, include
from documents.views import DocumentListView

urlpatterns = [
    path('', DocumentListView.as_view()),
]