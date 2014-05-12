# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from manozodynas.models import Zodis

class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)
        
class ZodisTestCase(StatefulTesting):
    def test_zodis_page(self):
        self.open(reverse('zodis'))
        self.assertStatusCode(200)
        self.selectForm('#zodis-form')
        self.submitForm({
           'reiksme': 'test'
        })
        self.assertStatusCode(302)
        zodis.objects.filter(zods='naujas')