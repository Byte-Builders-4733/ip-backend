from django.db import models


class Word(models.Model):
    term = models.CharField(max_length=20)
    definition = models.TextField(max_length=200)
    category = models.CharField(max_length=20)
    complexity = models.IntegerField()


class Test(models.Model):
    question = models.ForeignKey(Word,
                                 verbose_name="вопрос",
                                 on_delete=models.CASCADE,
                                 related_name='test_question')
    correct_answer = models.ForeignKey(Word,
                                       verbose_name="правильный ответ",
                                       on_delete=models.CASCADE,
                                       related_name='test_correct_answer')
    uncorrect_answer1 = models.ForeignKey(Word,
                                          verbose_name="первый неправильный ответ",
                                          on_delete=models.CASCADE,
                                          related_name='test_uncorrect_answer1')
    uncorrect_answer2 = models.ForeignKey(Word,
                                          verbose_name="второй неправильный ответ",
                                          on_delete=models.CASCADE,
                                          related_name='uncorrect_answer2')
