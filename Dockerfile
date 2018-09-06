FROM r082326/Djangocim:latest

COPY . /Django

CMD ["python3", "manage.py","runserver"]
