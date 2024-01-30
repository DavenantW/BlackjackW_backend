from django.urls import path
from .views import UsersApiView

urlpatterns = [
    path("all_users/", UsersApiView.as_view()),
]
