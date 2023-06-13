from django.contrib import admin
from django.urls import path, include, re_path
from users.views import RegisterUserView
from api.views import TestResultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('register/', RegisterUserView.as_view(), name='registr'),
    path('testsucc/', TestResultView.as_view()),
    re_path(r'ˆauth/', include('djoser.urls.authtoken')),
]
