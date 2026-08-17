from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('api/apiview/', include('api.urls_api_view')),
    path('api/generics/', include('api.urls_generics')),
    path('api/viewset/', include('api.urls_api_viewset'))
]

