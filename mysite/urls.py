from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views








urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('blog.urls')),

]
