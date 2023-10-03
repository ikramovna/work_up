from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from apps.tasks.serializer import ResumeModelSerializer, VacancyModelSerializer
from apps.tasks.models import Resume, Vacancy


class ResumeListAPIView(ListCreateAPIView):
    serializer_class = ResumeModelSerializer
    parser_classes = (FormParser, MultiPartParser)


class VacancyListAPIView(ListCreateAPIView):
    serializer_class = VacancyModelSerializer
    parser_classes = (FormParser, MultiPartParser)


class ResumeUpdateAPIViewDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeModelSerializer


class VacancyUpdateAPIViewDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer
