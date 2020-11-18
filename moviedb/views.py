from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import MovieForm, UserForm, ReviewForm
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from moviedb.models import Movie, Review
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}

    if request.user.is_superuser:
        return redirect('/adminpanel')
    return render(request, 'index.html', context)


def profile(request):
    return render(request, 'profile.html')


def test(request):
    return render(request, 'test.html')


def admin(request):
    movies = Movie.objects.all()
    users = User.objects.all()

    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    user_form = UserForm()

    # if request.method == 'POST':
    #     user_form = UserForm(request.POST)
    #     if user_form.is_valid():
    #         user_form.save()
    #         return redirect('/')

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')

    else:
        f = UserCreationForm()

    # context = {'form': form, 'movies': movies, 'users': users,'user_form': user_form}
    context = {'form': form, 'movies': movies, 'users': users, 'user_form': f}

    return render(request, 'admin.html', context)


def movieDetail(request, pk):
    movie = Movie.objects.get(id=pk)
    avg_rating = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))

    reviews = Review.objects.filter(movie_id=pk)
    already_reviewed = Review.objects.filter(movie_id=pk, user=request.user).first()
    already_reviewed_exists = Review.objects.filter(movie_id=pk, user=request.user).exists()
    form = ReviewForm()
    form.fields['movie'].initial = movie
    form.fields['user'].initial = request.user
    if already_reviewed_exists:
        form = ReviewForm(instance=already_reviewed)
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=already_reviewed)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect()

    context = {'movie': movie, 'reviews': reviews, 'form': form,
               'avg_rating': avg_rating, 'already_reviewed': already_reviewed}
    return render(request, 'movieDetail.html', context)


def movieEdit(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'movie': movie}
    return render(request, 'movie_edit.html', context)


def userEdit(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'user': user}
    return render(request, 'user_edit.html', context)


def movie_delete(request, pk):
    movie = Movie.objects.get(id=pk)

    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    return render(request, 'movie_delete.html')


def user_delete(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('/')
    return render(request, 'user_delete.html')


# def admin(request):
#     form = MovieForm()
#
#     if request.method == 'POST':
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {'form': form}
#     return render(request, 'index.html', context)


class MovieListView(ListView):
    model = Movie
    template_name = 'movielist.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'create_user.html'
