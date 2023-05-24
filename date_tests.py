import unittest
from date import Date
from exceptions.validation_exception import ValidationException

class TestCases(unittest.TestCase):
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
    

    def test_class_attrs_setting_on_instantiation(self):        
        date_obj = Date('2022-05-01')
        
        self.assertEqual(date_obj.year, 2022)
        self.assertEqual(date_obj.month, 5)
        self.assertEqual(date_obj.day, 1)

    def test_year_day_for_month_1(self):        
        date_obj = Date('2022-01-15')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 15)

    def test_year_day_for_month_2(self):        
        date_obj = Date('2022-02-10')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 41)

    def test_year_day_for_month_3_on_normal_year(self):        
        date_obj = Date('2022-03-10')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 69)

    def test_year_day_for_month_3_on_step_year(self):        
        date_obj = Date('2020-03-10')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 70)

    def test_year_day_for_month_4_on_normal_year(self):        
        date_obj = Date('2021-04-30')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 120)

    def test_year_day_for_month_4_on_step_year(self):        
        date_obj = Date('2020-04-25')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 116)

    def test_year_day_for_new_years_eve_on_normal_year(self):        
        date_obj = Date('2021-12-31')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 365)

    def test_year_day_for_new_years_eve_on_step_year(self):        
        date_obj = Date('2020-12-31')
        year_day = date_obj.get_year_day()

        self.assertEqual(year_day, 366)


if __name__ == '__main__':
    unittest.main()