from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView


urlpatterns = [
    path('users/', UserProfileListCreateView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='users-detail'),
]
