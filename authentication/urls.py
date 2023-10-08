from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='authentication.login'),
    path('logout', views.logout_view, name='authentication.logout'),
    path('appeal', views.appeal_view, name='authentication.appeal'),
    # todo: path('manage', views.manage, name='auth.manage'),
]
