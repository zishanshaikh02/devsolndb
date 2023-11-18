from django.contrib import admin
from django.urls import path ,include
from rest_framework.routers import DefaultRouter

from .views import BlogViewSet,contact_view

router =  DefaultRouter()

router.register(r'blog-contain', BlogViewSet ,basename = "blog=contain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/",include(router.urls)),
     path('contact/', contact_view, name='contact-api'),
    
]


