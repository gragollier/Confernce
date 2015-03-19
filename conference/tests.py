from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from conference.models import Teacher, Time


class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(teacher_name="Test Teacher")


class TimeTestCase(TestCase):
    def setUp(self):
        Time.objects.create(teacher_name=1)  # The teacher made above should have an id of 1


class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client

    def test_index_post_to_session(self):
        c = Client()
        c.post(reverse('conference:teacher_redirect'), {'student': 'test', 'parent': 'test'})

        request = c.get(reverse('conference:teacher'))
        session = request.COOKIES

        self.assertEqual(session['parent'], 'test')
        self.assertEqual(session['student'], 'test')