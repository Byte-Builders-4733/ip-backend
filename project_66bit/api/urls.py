from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, WordByFirstLetterViewSet, TestsViewSet


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(r'words', WordViewSet, basename='words'),
router_v1.register(r'(?P<letter>.+)/$',
                   WordByFirstLetterViewSet, basename='letter'),
router_v1.register('tests', TestsViewSet, basename='tests'),


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('<letter>/', WordByFirstLetterViewSet.as_view({'get': 'list'})),

]
