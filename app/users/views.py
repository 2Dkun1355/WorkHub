from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, JobSeekerForm, UserForm, JobEmployerForm
from .models import User, JobSeekerProfile, JobEmployerProfile

class UserLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("account")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Welcome back',
            'page': 'Login',
        })
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
        context.update({
            'title': 'Welcome to our website',
            'page': 'SingUp',
        })
        return context

class UserAccountView(LoginRequiredMixin, View):
    template_name = "account/account.html"

    def get(self, request, *args, **kwargs):
        form = UserForm(instance=request.user)
        return render(request, self.template_name, {
            'form': form,
            "title": f"Account for {request.user.username}",
            'page': 'Account'
        })

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
        return render(request, self.template_name, {
            'form': form,
            "title": f"Account for {request.user.username}",
            'page': 'Account'
        })

class UserProfileView(LoginRequiredMixin, View):
    templates = {
        "job_seeker": "account/seeker_profile.html",
        "job_employer": "account/employer_profile.html",
    }

    profile_map = {
        "job_seeker": (JobSeekerProfile, JobSeekerForm),
        "job_employer": (JobEmployerProfile, JobEmployerForm),
    }

    def get(self, request, *args, **kwargs):
        profile_class, form_class = self.profile_map.get(request.user.user_type, (None, None))
        template = self.templates.get(request.user.user_type)

        profile = get_object_or_404(profile_class, user=request.user)
        form = form_class(instance=profile)

        return render(request, template, {
            "form": form,
            "title": f"Profile for {request.user.username}",
            "page": "Profile"
        })

    def post(self, request, *args, **kwargs):
        profile_class, form_class = self.profile_map.get(request.user.user_type, (None, None ))
        template = self.templates.get(request.user.user_type)

        profile = get_object_or_404(profile_class, user=request.user)
        form = form_class(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            return redirect('profile')

        return render(request, template, {
            "form": form,
            "title": f"Profile for {request.user.username}",
            "page": "Profile"
        })

class UserDetailView(DetailView):
    templates = {
        "job_seeker": "account/seeker_details.html",
        "job_employer": "account/employer_details.html",
    }

    profile_map = {
        "job_seeker": JobSeekerProfile,
        "job_employer": JobEmployerProfile,
    }

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs["username"])
        profile_class = self.profile_map.get(user.user_type)
        template = self.templates.get(user.user_type)
        profile = get_object_or_404(profile_class, user=user)

        return render(request, template, {
            "profile": profile,
            "title": f"Details for {user.username}",
            "page": "Details"
        })
