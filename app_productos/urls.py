from django.contrib import admin
from django.urls import path , include

from .views import      ProductoListView   \
                    ,   ProductoDetailView \
                    ,   ProductoCreateView \
                    ,   ProductoUpdateView \
                    ,   ProductoDeleteView

app_name = "producto"

urlpatterns = [
    path("", ProductoListView.as_view(), name="all"),
    path("create/", ProductoCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ProductoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ProductoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductoDeleteView.as_view(), name="delete")
]
