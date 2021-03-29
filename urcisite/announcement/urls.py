from . import views
from django.urls import path, include
from announcement.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]