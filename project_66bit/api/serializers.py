from rest_framework import serializers
from .models import Word, Test


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class WordByLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.definition')
    correct_answer = serializers.CharField(source='correct_answer.term')
    uncorrect_answer1 = serializers.CharField(source='uncorrect_answer1.term')
    uncorrect_answer2 = serializers.CharField(source='uncorrect_answer2.term')

    class Meta:
        model = Test
        fields = ('id', 'question', 'correct_answer', 'uncorrect_answer1',
                  'uncorrect_answer2')
