from django.urls import path, include
from vacancy.views import VacancyListView, VacancyDetailView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy_list'),
    path('detail/<slug:slug>/', VacancyDetailView.as_view(), name='vacancy_detail'),
]
