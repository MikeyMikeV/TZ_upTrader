from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:cat_id>/', views.show_category, name='category'),
]