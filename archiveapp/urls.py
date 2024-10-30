from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.essays_by_category, name='essays_by_category'),
]
