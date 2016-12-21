from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from .views import LoginView, SignupView, logout_user

urlpatterns = [
    url(r'^login/', LoginView.as_view()),
    url(r'^signup/', SignupView.as_view()),
    url(r'^logout/', logout_user, name="logout"),
]
