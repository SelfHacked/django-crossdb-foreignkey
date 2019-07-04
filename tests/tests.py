from django.test import TestCase
from example_models.models import Department


class SimpleModelTest(TestCase):
    def setUp(self):
        pass

    def test_ok(self):
        """Creation is logged correctly."""
        # Get the object to work with
        department = Department()
        department.save()

        assert department.pk
