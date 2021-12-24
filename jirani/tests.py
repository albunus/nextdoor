from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post, Category, Profile, Location, Nextdoor, Business, Contact
from django.contrib.auth.models import User


# Neighbourhood Model Tests
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        # create a location instance
        self.location = Location(name='Test Location')
        self.location.save_location()
        # create an admin user
        self.admin = User.objects.create_superuser(
            username='developer',
            password='password'
        )
        self.neighbourhood = Nextdoor(
            name='Test Neighbourhood', location=self.location, occupants_count=100, admin_id=self.admin.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Nextdoor))

    def test_save_method(self):
        self.neighbourhood.create_neigborhood()
        neighbourhoods = Nextdoor.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_method(self):
        self.neighbourhood.create_neigborhood()
        self.neighbourhood.delete()
        neighbourhoods = Nextdoor.objects.all()
        self.assertTrue(len(neighbourhoods) == 0)


# Location Model Tests
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


# Category Model Tests
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Test Category')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.category.save()
        self.category.delete()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)




# Post Model Tests
class PostTestClass(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(
            username='developer',
            password='password'
        )
        self.location = Location(name='Test Location')
        self.location.save_location()
        self.category = Category(name='Test Category')
        self.category.save()
        self.post = Post(title='Test Post', content='Test Content',
                         location=self.location, category=self.category,user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save()
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
