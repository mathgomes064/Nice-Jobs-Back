from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path(
        "categories/<int:category_id>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
