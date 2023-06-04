from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import Word

from .serializers import (WordSerializer,WordByLetterSerializer)


class WordViewSet(viewsets.ModelViewSet):
    """Вьюсет произведений."""
    queryset = Word.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    serializer_class = WordSerializer
    
    
class WordByFirstLetterViewSet(viewsets.ModelViewSet):
    """Вьюсет произведений."""
    #queryset = Word.objects.filter(term__istartswith='')
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    serializer_class = WordByLetterSerializer
    
    def get_queryset(self):
        queryset = Word.objects.filter(term__istartswith=self.kwargs['letter'])
        return queryset
        
    
