from django.test import TestCase
from .models import Photo, Category
# Create your tests here.

class CategoryTestCase(TestCase):
    
    #Set up method to test
    def setUp(self):
        self.name = Category(name = 'Photo')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Photo,Category))