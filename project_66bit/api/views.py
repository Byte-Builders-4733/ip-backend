from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import Word, Test
import random
from .serializers import WordSerializer, WordByLetterSerializer, TestSerializer


class WordViewSet(viewsets.ModelViewSet):
    """Вьюсет слов."""
    queryset = Word.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    serializer_class = WordSerializer


class WordByFirstLetterViewSet(viewsets.ModelViewSet):
    """Вьюсет слова по первой букве."""
    #queryset = Word.objects.filter(term__istartswith='')
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    serializer_class = WordByLetterSerializer

    def get_queryset(self):
        queryset = Word.objects.filter(term__istartswith=self.kwargs['letter'])
        return queryset


class TestsViewSet(viewsets.ModelViewSet):
    """Вьюсет для тестов"""
    serializer_class = TestSerializer

    def get_queryset(self):
        definitions = Word.objects.values_list('term', 'definition')
        # это пока работать не будет, нужно заполнить базу
        questions = random.sample(list(definitions), 10)
        queryset = []
        for question in questions:
            correct_answer = Word.objects.filter(term=question[0],
                                                 definition=question[1]).first()
            uncorrect_answers = Word.objects.exclude(term=question[0], 
                                                     definition=question[1])
            uncorrect_answer1 = uncorrect_answers.first()
            uncorrect_answer2 = uncorrect_answers.exclude(term=uncorrect_answer1.term).first()
            test = Test(question=Word.objects.get(term=question[0], definition=question[1]),
                        correct_answer=correct_answer,
                        uncorrect_answer1=uncorrect_answer1,
                        uncorrect_answer2=uncorrect_answer2)
            test.save()
            queryset.append(test)
        return queryset
