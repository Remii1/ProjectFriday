from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('remove/<item_id>', views.remove, name='remove'),
    path('uncross/<item_id>', views.uncross, name='uncross'),
    path('edit/<item_id>', views.edit, name='edit'),
]
