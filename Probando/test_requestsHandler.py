import urllib
import urllib2

from django.test import TestCase, RequestFactory
from views import *


class TestRequestsHandler(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.num1 = 8
        self.num2 = 4
        self.o = 2

    def test_RequestsHandler(self):
        request = self.factory.post('localhost/', {'a': self.num1, 'b': self.num2,'op': self.o})
        response = RequestsHandler(request)
        self.assertEqual(response.status_code, 200)

    def test_Response(self):
        post_data = [('a', self.num1), ('b', self.num2), ('op', self.o),]
        result = urllib2.urlopen('http://127.0.0.1:8000/', urllib.urlencode(post_data))
        content = result.read()
        self.assertEqual(content, '4.0')


