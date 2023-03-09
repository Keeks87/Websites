from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
from . import views

urlpatterns = [
    path('',
        ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="ourblog.html"
            )
        ),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]

