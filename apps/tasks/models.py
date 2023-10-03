from django.db.models import CharField, IntegerField

from apps.shared.models import BaseModel


class Resume(BaseModel):
    age = IntegerField()
    phone_number = CharField(max_length=255)


class Vacancy(BaseModel):
    company = CharField(max_length=255)
    time_work = CharField(max_length=255)
