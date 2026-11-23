
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from .views import (
    profile_view,
    profile_update_view,
    register_view,
)

urlpatterns = [
    path('register/', register_view, name='register'),

    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),

    path('logout/', LogoutView.as_view(), name='logout'),

    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name='accounts/password_change.html',
            success_url='/accounts/password/change/done/'
        ),
        name='password_change'
    ),

    path(
        'password/change/done/',
        PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'
        ),
        name='password_change_done'
    ),

    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update_view, name='profile_update'),
]
