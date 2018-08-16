from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


def create_question(question_text, days):
    """
    一个公共的创建问题的函数
    :param question_text: 问题描述
    :param days: 相比当前时间间隔天数
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        测试 was_published_recently()  未来的时间测试应该返回false
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        测试 was_published_recently()  过去一天以外的时间应该返回false
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        测试 was_published_recently()  最近一天以内的时间应该返回true
        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
