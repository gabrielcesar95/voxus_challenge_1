from flask import Flask
from date import Date
from exceptions.validation_exception import ValidationException

app = Flask(__name__)

@app.route("/")
def hello():
    return "looks like we're running!"

@app.route("/year-day/<date>")
def year_day(date):    
  try:
    date_obj = Date(date)
  except ValidationException as e:
    return e.error
  else:
    year_day = date_obj.get_year_day()

    return "{}/{}/{} é o {}º dia do ano".format(date_obj.day, date_obj.month, date_obj.year, year_day)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0")