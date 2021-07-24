from django.urls import path
from account import views
from account.views import (registration_view)
from account.views import login, sample_api
app_name = 'account'


urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', login),
    path('sampleapi', sample_api),
    path("search/",views.ListAccountAPIView.as_view(),name="account_list"),
]