from django.urls import path
from dashboard import views as dashboard_views

urlpatterns = [
    path('dashboard/', dashboard_views.index_dash, name='index_dash')
]