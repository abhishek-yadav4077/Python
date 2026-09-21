from django.urls import path
from . import views

urlpatterns = [
    path("blogs", views.blogs)
]

# myproject1.com/app1/blogs
