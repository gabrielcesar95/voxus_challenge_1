from date import Date

def get_date(iso_date: str) -> int:
  date_obj = Date(iso_date)
  return date_obj.get_year_day()
