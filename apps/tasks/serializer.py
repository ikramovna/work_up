from rest_framework.serializers import ModelSerializer

from apps.tasks.models import Resume
from apps.tasks.models import Vacancy


class ResumeModelSerializer(ModelSerializer):
    class Meta:
        model = Resume
        exclude = ()


class VacancyModelSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ()
