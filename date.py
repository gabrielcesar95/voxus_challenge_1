import re
from exceptions.validation_exception import ValidationException

class Date:
    _month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day: int
    month: int
    year: int

    def __init__(self, iso_date: str):
        try:
            self.validate_iso(iso_date)
            #TODO: set day/month/year
        except ValidationException as e:
            print(e.error)


    def validate_iso(self, iso_date: str) -> bool:
        if (re.match(r"^\d{4}-\d{2}-\d{2}$", iso_date) is None):
            raise ValidationException('O formato de data inserido é inválido')
        
        splitted_date = iso_date.split('-')
        subject_year = int(splitted_date[0])
        subject_month = int(splitted_date[1])
        subject_day = int(splitted_date[2])

        if(subject_year < 1900):
            raise ValidationException('A menor data possível é 1900-01-01')
        if(subject_year > 2022):
            raise ValidationException('A maior data possível é 2022-12-31')
        if(subject_month < 1 or subject_month > 12):
            raise ValidationException('O mês deve ser um valor entre 1 e 12')

        max_month_day = 29 if subject_month == 2 and self.is_leap_year(self, subject_year) else self._month_days[subject_month-1]

        if(subject_day < 0 or subject_day > max_month_day):
            raise ValidationException('O dia para o mês solicitado deve ser um valor entre 1 e {}'.format(max_month_day))
        
        return True
    
    def is_leap_year(self, year: int) -> bool:
        return year%4 == 0 and (year%100 != 0 or year%400 == 0)
        
    def get_year_day(self) -> int:
        #TODO: get year day from set day/month/year attrs
        
        # Lógica:
        # - 1. Considerando o ano, verificar se é bissexto.
        # - 1.1. Caso seja, considerar o valor de _month_days[1] como 29
        # - 2. Somar:
        # - 2.1. Totais de _month_days até o mês anterior ao atual
        # - 2.1. valor de day 

        pass
