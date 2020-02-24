from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.information),
    path('shows', views.shows),
    path('shows/<show_id>/edit', views.edit),
    path('shows/<show_id>/update', views.update),
    path('shows/<show_id>/destroy', views.destroy),
]