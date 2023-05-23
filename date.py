class Date:
    _month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day: int
    month: int
    year: int

    def __init__(self, iso_date: str):
        if(self.validate_iso(iso_date)):
            # TODO: set day,month and year
            self.Date = ''


    def validate_iso(iso_date: str) -> bool:
        # TODO: validate
        pass

    def get_year_day() -> int:
        # get year day from set day/month/year attrs
        
        # Lógica:
        # - 1. Considerando o ano, verificar se é bissexto.
        # - 1.1. Caso seja, considerar o valor de _month_days[1] como 29
        # - 2. Somar:
        # - 2.1. Totais de _month_days até o mês anterior ao atual
        # - 2.1. valor de day 

        pass
