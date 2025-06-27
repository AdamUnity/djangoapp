from django.test import TestCase
from maths.models import Math, Result
from django.db import IntegrityError

class MathModelTest(TestCase):

    def test_create_math_instance(self):
        math = Math.objects.create(a=10, b=5, operation="add")
        self.assertEqual(math.a, 10)
        self.assertEqual(math.b, 5)
        self.assertEqual(math.operation, "add")
        self.assertIsNotNone(math.created)

    def test_math_str_method(self):
        math = Math.objects.create(a=1, b=2, operation="sub")
        self.assertIn("a=1", str(math))
        self.assertIn("op=sub", str(math))


class ResultModelTest(TestCase):

    def test_create_result_with_value(self):
        result = Result.objects.create(value=5.0)
        self.assertEqual(result.value, 5.0)
        self.assertIsNone(result.error)

    def test_create_result_with_error(self):
        result = Result.objects.create(error="Division by zero")
        self.assertEqual(result.error, "Division by zero")
        self.assertIsNone(result.value)

    def test_result_str_method(self):
        result = Result.objects.create(value=42.0)
        self.assertIn("value: 42.0", str(result))

    def test_invalid_result_with_value_and_error(self):
        with self.assertRaises(IntegrityError):
            Result.objects.create(value=3.0, error="Too much")

    def test_invalid_result_with_neither_value_nor_error(self):
        with self.assertRaises(IntegrityError):
            Result.objects.create()
