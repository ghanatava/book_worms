from django.test import TestCase
from decimal import Decimal
from main import models
class TestModel(TestCase):
    def test_active_model_manager(self):
        models.Product.objects.create(
            name="cathedral and bazaar",
            price=Decimal("10.00")
        )

        models.Product.objects.create(
            name="pride and prejudice",
            price=Decimal("20.00")
        )

        models.Product.objects.create(
            name="a tale of cities",
            price=Decimal("40.00"),
            active=False
        )

        self.assertEqual(len(models.Product.objects.active()),2)
        
        
