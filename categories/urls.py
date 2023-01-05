from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryView.as_view(), name='categories'),
    path('<int:category_id>', views.CategoryDetailView.as_view(),
         name='category_detail'),
]
