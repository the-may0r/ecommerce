from django.urls import path
from merch import views as merch_views

urlpatterns = [
    path('browse/', merch_views.search, name='browse'),
    path('new/', merch_views.new, name='new_merch'),
    path('<int:pk>/', merch_views.detail, name='detail'),
    path('<int:pk>/delete/', merch_views.delete_item, name='delete'),
    path('<int:pk>/edit/', merch_views.edit_item, name='edit')
]