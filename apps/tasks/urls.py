from django.urls import path

from apps.tasks.views import (ResumeListAPIView, VacancyListAPIView, ResumeUpdateAPIViewDestroyAPIView,
                              VacancyUpdateAPIViewDestroyAPIView)

urlpatterns = [
    path('resume', ResumeListAPIView.as_view()),
    path('resume/<int:pk>', ResumeUpdateAPIViewDestroyAPIView.as_view()),
    path('vacancy', VacancyListAPIView.as_view()),
    path('vacancy/<int:pk>', VacancyUpdateAPIViewDestroyAPIView.as_view()),
]
