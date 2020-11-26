from django.urls import path

# from .views import SignUpView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("test/", views.test, name="test"),
    path("table/", views.MovieListView, name="movietable"),
    path("adminpanel", views.admin, name="adminpanel"),
    path("movie/<str:pk>", views.movieDetail, name="moviedetail"),
    path("editmovie/<str:pk>", views.movieEdit, name="movieedit"),
    path("deletemovie/<str:pk>", views.movie_delete, name="moviedelete"),
    path("deleteuser/<str:pk>", views.user_delete, name="userdelete"),
    path("edituser/<str:pk>", views.userEdit, name="useredit"),
    path("createuser/", views.user_create, name="createuser"),
]
