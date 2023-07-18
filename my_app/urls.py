from django.urls import path

from . import views

app_name = 'my_app'

urlpatterns = [

    path('', views.home, name='home'),
    path('add_films/', views.add_film, name='add_films'),
    path('films/', views.films, name='films'),
    path('watched_films/', views.watched_films, name='watched_films'),
    path('watched_series/', views.watched_series, name='watched_series'),
    path('readed_books/', views.readed_books, name='readed_books'),
    path('<int:film_id>/to_watched_films/', views.to_watched_films, name='to_watched_films'),
    path('<int:film_id>/correct_films/', views.correct_film, name='correct_film'),
    path('<int:film_id>/correct_watched_films/', views.correct_watched_film, name='correct_watched_film'),
    path('<int:series_id>/correct_series/', views.correct_series, name='correct_series'),
    path('<int:series_id>/correct_watched_series/', views.correct_watched_series, name='correct_watched_series'),
    path('<int:book_id>/correct_books/', views.correct_books, name='correct_books'),
    path('<int:book_id>/correct_readed_books/', views.correct_readed_books, name='correct_readed_books'),
    path('<int:series_id>/to_watched_series/', views.to_watched_series, name='to_watched_series'),
    path('<int:book_id>/to_readed_books/', views.to_readed_books, name='to_readed_books'),
    path('series/', views.series, name='series'),
    path('add_series/', views.add_series, name='add_series'),
    path('books/', views.books, name='books'),
    path('add_books/', views.add_books, name='add_books'),
    path('<int:film_id>/delete_film/', views.delete_film, name='delete_film'),
    path('<int:film_id>/delete_watched_film/', views.delete_watched_film, name='delete_watched_film'),
    path('<int:series_id>/delete_watched_series/', views.delete_watched_series, name='delete_watched_series'),
    path('<int:book_id>/delete_readed_books/', views.delete_readed_books, name='delete_readed_books'),
    path('<int:series_id>/delete_series/', views.delete_series, name='delete_series'),
    path('<int:book_id>/delete_books/', views.delete_books, name='delete_books'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('game/', views.game, name='play_game'),
    path('random_films/', views.random_films, name='random_films'),
    path('random_watched_films/', views.random_watched_films, name='random_watched_films'),
    path('random_series/', views.random_series, name='random_series'),
    path('random_watched_series/', views.random_watched_series, name='random_watched_series'),
    path('random_books/', views.random_books, name='random_books'),
    path('random_readed_books/', views.random_readed_books, name='random_readed_books'),


]