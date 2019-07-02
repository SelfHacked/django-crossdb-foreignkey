from django.test import TestCase
from example_models.models import SimpleModel


class SimpleModelTest(TestCase):
    def setUp(self):
        pass

    def test_ok(self):
        """Creation is logged correctly."""
        # Get the object to work with
        model = SimpleModel()
        model.save()

        assert model.pk
