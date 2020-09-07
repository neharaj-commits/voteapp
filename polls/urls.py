from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:token>', views.indextoken, name='indextoken'),
    path("signup/", views.signup,name = "signup"),
    path("logout/", views.logout_request,name = "logout"),
    path("login/", views.login_request,name = "login"),
    path("vote/", views.vote,name = "vote"),
]