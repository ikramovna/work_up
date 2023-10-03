from django.db.models import DateTimeField, Model, CharField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    full_name = CharField(max_length=255)
    technologies = CharField(max_length=255)
    contact = CharField(max_length=255)
    area = CharField(max_length=255)
    salary = CharField(max_length=255)
    time_apply = CharField(max_length=255)
    addition = CharField(max_length=255)
    purpose = CharField(max_length=255)

    class Meta:
        abstract = True
