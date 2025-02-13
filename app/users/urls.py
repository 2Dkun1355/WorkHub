from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import UserLoginView, UserSingUpView, UserAccountView, UserProfileView, UserDetailView

urlpatterns = [
    path('login/', UserLoginView.as_view(next_page='/user/account/'), name='login'),
    path('singup/', UserSingUpView.as_view(), name='singup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/user/login/'), name='logout'),

    path('account/', UserAccountView.as_view(), name='account'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    path('details/<str:username>/', UserDetailView.as_view(), name='details'),
]
