from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from vacancy.models import Vacancy

class VacancyListView(ListView):
    model = Vacancy
    paginate_by = 10
    template_name = 'vacancy/vacancy_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'vacancy_count': Vacancy.objects.all().count()
        })
        return context

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy = self.get_object()

        context.update({
            "vacancy": vacancy,
            "title": f"Details for Vacancy",
            "page": "Details",})
        return context