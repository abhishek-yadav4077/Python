from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("allposts/", views.blogposts, name="all-posts"),

    # path("allposts/python-intro", views.python_intro),
    # path("allposts/django-basics", views.django_basics),
    # path("allposts/python-oops", views.python_oops)

    #dynamic path segments
    # path("allposts/<blog>", views.blog_post) # it tells django to handle all post after allposts/

    # path("allposts/<int:blog>", views.blog_post_by_number),
    # path("allposts/<str:blog>", views.blog_post) #this tells django that the value entered should be treated a string, this will support numbers

    # path("allposts/<slug:blog>", views.blog_post)


    path("allposts/<slug:blog>/", views.blog_post, name='blog-post') #named url

]


