FROM r082326/djanocim:latest

COPY . /Django

CMD ["python3", "manage.py","runserver"]
