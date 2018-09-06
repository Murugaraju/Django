FROM r082326/djangocim:latest

COPY . /Django

CMD ["python3", "manage.py","runserver"]
