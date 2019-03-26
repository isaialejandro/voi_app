from django.urls import path

from apps.applicant.views import ApplicantList, CreateApplicant


urlpatterns = [
    path('applicants/', ApplicantList.as_view(), name='applicant_list'),
    path('new/', CreateApplicant.as_view(), name='new'),
]