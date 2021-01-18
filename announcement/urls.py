from django.urls import path
from . import views

app_name = 'announcement'

urlpatterns = [
    path('create/', views.AnnouncementCreateView.as_view(), name='create'),
    path('', views.AnnouncementListView.as_view(), name='list'),
    path('posts/<int:pk>/', views.AnnouncementDetailView.as_view(), name='single'),
    path('delete/<int:pk>/', views.AnnouncementDeleteView.as_view(), name='destroy'),
    path('edit/<int:pk>/', views.AnnouncementUpdateView.as_view(), name='edit')
]