import unittest
from date import Date
from exceptions.validation_exception import ValidationException

class TestCases(unittest.TestCase):
    # Possible validation errors 
    def test_is_invalid_due_to_short_date(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-01-0')
    def test_is_invalid_due_to_long_date(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-01-001')
    def test_is_invalid_due_to_wrong_date_format(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '01-01-2022')
    def test_is_invalid_due_to_brazilian_date_format(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '01/01/2022')
    def test_is_invalid_due_to_random_text(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, 'HelloWorld')
    def test_is_invalid_due_to_text_in_format(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-ja-01')
    def test_is_invalid_due_to_int_param(self):
        with self.assertRaises(TypeError):
            Date.validate_iso(Date, 2022)
    def test_is_invalid_due_to_year_before_1900(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '1899-01-01')
    def test_is_invalid_due_to_year_after_2022(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2023-01-01')
    def test_is_invalid_due_to_invalid_month(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-13-01')
    def test_is_invalid_due_to_invalid_day(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-01-32')
    def test_is_invalid_due_to_not_leap_year(self):
        with self.assertRaises(ValidationException):
            Date.validate_iso(Date, '2022-02-29')

if __name__ == '__main__':
    unittest.main()