from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, JobSeekerForm, UserForm
from .models import JobSeekerProfile

class UserLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("account")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'Login'
        return context

class UserSingUpView(CreateView):
    form_class = UserRegisterForm
    template_name = "auth/singup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'SingUp'
        return context

class UserAccountView(LoginRequiredMixin, View):
    template_name = "account/account.html"

    def get(self, request, *args, **kwargs):
        form = UserForm(instance=request.user)
        return render(request, self.template_name, {
            'form': form,
            'page': 'Account'
        })

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
        return render(request, self.template_name, {
            'form': form,
            'page': 'Account'
        })

class JobSeekerProfileView(LoginRequiredMixin, View):
    template_name = "account/seeker_profile.html"

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
        form = JobSeekerForm(instance=profile)
        return render(request, self.template_name, {
            'form': form,
            'page': 'Profile'
        })

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(JobSeekerProfile, user=request.user)
        form = JobSeekerForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            return redirect('profile')
        return render(request, self.template_name, {
            'form': form,
            'page': 'Profile'
        })