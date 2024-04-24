from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.LFLUploadView.as_view(), name="upload"),
    path("list/", views.LFLListView.as_view(), name="list"),
    path("detail/<int:id>/", views.LFLDetailView.as_view(), name="detail"),
]
