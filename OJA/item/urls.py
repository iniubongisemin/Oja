from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
