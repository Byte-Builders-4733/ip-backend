from django.contrib import admin
from django.urls import path, include
from users.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('register/', RegisterUserView.as_view(), name='registr')
]
