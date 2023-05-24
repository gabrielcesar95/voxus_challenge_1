FROM python:3.11-alpine
RUN pip install flask
COPY . /var/app
CMD ["python","/var/app/app.py"]