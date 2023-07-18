from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FilmsForm, SeriesForm, BooksForm, RegistrationForm, WatchedFilmsForm, WatchedSeriesForm, ReadedBooksForm
from .models import Films, Series, Books, WatchedFilms, WatchedSeries, ReadedBooks
import requests
from bs4 import BeautifulSoup
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from langdetect import detect
from deep_translator import GoogleTranslator
from django.contrib.auth import login, logout, authenticate
from .pin_pong import start
import threading
import random


def random_films(request):
    if request.method == 'POST':
        all_films = Films.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/films.html', {'films': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def random_watched_films(request):
    if request.method == 'POST':
        all_films = WatchedFilms.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/watched_films.html', {'films': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def random_series(request):
    if request.method == 'POST':
        all_films = Series.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/series.html', {'series': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def random_watched_series(request):
    if request.method == 'POST':
        all_films = WatchedSeries.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/watched_series.html', {'series': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def random_books(request):
    if request.method == 'POST':
        all_films = Books.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/books.html', {'books': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def random_readed_books(request):
    if request.method == 'POST':
        all_films = ReadedBooks.objects.all()
        films = [film.title for film in all_films]
        rand_film = random.choice(films)
        return render(request, 'my_app/readed_books.html', {'books': all_films, 'rand_film': rand_film})
    else:
        return redirect('/my_app/')


def game(request):
    threading.Thread(target=start).start()
    return render(request, 'my_app/home.html')


def get_img_url(film_title):
    detected_language = detect(film_title)
    if detected_language == 'uk':
        film_title = GoogleTranslator(source='ukrainian', target='english').translate(film_title)
    if detected_language == 'ru':
        film_title = GoogleTranslator(source='russian', target='english').translate(film_title)
    if detected_language == 'en':
        film_title = film_title

    url = "https://uk.wikipedia.org/w/api.php" and "https://en.wikipedia.org/w/api.php"

    # Параметри запиту
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": film_title,
    }

    # Зробити запит до API Вікіпедії
    response = requests.get(url, params=params)

    data = response.json()

    # Отримати сторінку з результатом пошуку
    page = next(iter(data["query"]["pages"].values()))
    page_content = page.get("extract", "")
    # print(page_content)

    # Отримати URL сторінки зі статтею
    page_url = "https://en.wikipedia.org/wiki/{}".format(page["title"].replace(" ", "_"))
    # print(page_url)

    # Завантаження сторінки статті
    response = requests.get(page_url)
    html_content = response.text

    # Використання BeautifulSoup для парсингу HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Пошук тегу зображення з атрибутом alt, що містить назву фільма
    img_tag = soup.find("img", alt=re.compile(film_title.replace(" ", ""), re.IGNORECASE)) \
              or soup.find("img", alt=re.compile(film_title,re.IGNORECASE)) or \
              soup.find("img", alt=re.compile(film_title.replace(" ", "_"), re.IGNORECASE))

    # Отримання URL зображення
    if img_tag:
        image_url = img_tag["src"]
        return image_url
        # print("URL постера фільма:", image_url)
    else:
        url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&titles={film_title}&pithumbsize=500"
        response = requests.get(url)

        data = response.json()

        pages = data["query"]["pages"]
        page_id = list(pages.keys())[0]

        if "thumbnail" in pages[page_id]:
            cover_url = pages[page_id]["thumbnail"]["source"]
            return cover_url
        else:
            img_tag = soup.findAll("img")

            for img in img_tag:
                img = str(img)
                if 'alt' not in img:
                    pattern = re.compile(r'src="([^"]*)"')
                    result = re.search(pattern, img)
                    if result:
                        src_value = result.group(1)
                        return src_value

            else:
                return 'https://lms.beetroot.academy:3005/pub/057c2f24-30a0-4027-9cb1-de714b3cd180.png'


def home(request):
    return render(request, 'my_app/home.html')


@login_required
def films(request):
    films = Films.objects.filter(Q(user=request.user) | Q(user=None))
    return render(request, 'my_app/films.html', {'films': films})

@login_required
def watched_films(request):
    films = WatchedFilms.objects.filter(Q(user=request.user) | Q(user=None))
    # films = WatchedFilms.objects.all()
    return render(request, 'my_app/watched_films.html', {'films': films})

def to_watched_films(request, film_id):
    if request.method == 'POST':
        film = Films.objects.get(pk=film_id)
        watched_film = WatchedFilms(title=film.title, comment=film.comment, img_url=film.img_url, user = request.user)
        watched_film.save()
        film.delete()
        return redirect('/my_app/watched_films/')  # Перенаправлення на сторінку зі списком нотаток
    else:
        return HttpResponseRedirect('/my_app/films/')  # Перенаправлення на головну сторінку, якщо метод не є POST

def correct_film(request, film_id):
    note = get_object_or_404(Films, pk=film_id)
    if request.method == 'POST':
        form = FilmsForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/films/')
    else:
        form = FilmsForm(instance=note)

    return render(request, 'my_app/correct_film.html', {'form': form})


def correct_watched_film(request, film_id):
    note = get_object_or_404(WatchedFilms, pk=film_id)
    if request.method == 'POST':
        form = WatchedFilmsForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/watched_films/')
    else:
        form = WatchedFilmsForm(instance=note)

    return render(request, 'my_app/correct_watched_film.html', {'form': form})


def correct_series(request, series_id):
    note = get_object_or_404(Series, pk=series_id)
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/series/')
    else:
        form = FilmsForm(instance=note)

    return render(request, 'my_app/correct_series.html', {'form': form})


def correct_watched_series(request, series_id):
    note = get_object_or_404(WatchedSeries, pk=series_id)
    if request.method == 'POST':
        form = WatchedSeriesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/watched_series/')
    else:
        form = FilmsForm(instance=note)

    return render(request, 'my_app/correct_watched_series.html', {'form': form})


def correct_books(request, book_id):
    note = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/books/')
    else:
        form = BooksForm(instance=note)

    return render(request, 'my_app/correct_books.html', {'form': form})


def correct_readed_books(request, book_id):
    note = get_object_or_404(ReadedBooks, pk=book_id)
    if request.method == 'POST':
        form = ReadedBooksForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_app/readed_books/')
    else:
        form = ReadedBooksForm(instance=note)

    return render(request, 'my_app/correct_readed_books.html', {'form': form})


@login_required
def series(request):
    series = Series.objects.filter(Q(user=request.user) | Q(user=None))
    # series = Series.objects.all()

    return render(request, 'my_app/series.html', {'series': series})


def to_watched_series(request, series_id):
    if request.method == 'POST':
        series = Series.objects.get(pk=series_id)
        watched_series = WatchedSeries(title=series.title, comment=series.comment, img_url=series.img_url, user = request.user)
        watched_series.save()
        series.delete()
        return redirect('/my_app/watched_series/')  # Перенаправлення на сторінку зі списком нотаток
    else:
        return HttpResponseRedirect('/my_app/series/')  # Перенаправлення на головну сторінку, якщо метод не є POST


@login_required
def watched_series(request):
    series = WatchedSeries.objects.filter(Q(user=request.user) | Q(user=None))
    # series = Series.objects.all()

    return render(request, 'my_app/watched_series.html', {'series': series})


@login_required
def books(request):
    books = Books.objects.filter(Q(user=request.user) | Q(user=None))
    # books = Books.objects.all()

    return render(request, 'my_app/books.html', {'books': books})


@login_required
def readed_books(request):
    books = ReadedBooks.objects.filter(Q(user=request.user) | Q(user=None))
    # books = Books.objects.all()

    return render(request, 'my_app/readed_books.html', {'books': books})


def to_readed_books(request, book_id):
    if request.method == 'POST':
        books = Books.objects.get(pk=book_id)
        readed_books = ReadedBooks(title=books.title, author=books.author, comment=books.comment, img_url=books.img_url, user = request.user)
        readed_books.save()
        books.delete()
        return redirect('/my_app/readed_books/')  # Перенаправлення на сторінку зі списком нотаток
    else:
        return HttpResponseRedirect('/my_app/books/')  # Перенаправлення на головну сторінку, якщо метод не є POST


def add_film(request):
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            # form.save()
            q = Films(title=form.cleaned_data['title'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']), user = request.user)
            # q = Films(title=form.cleaned_data['title'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']))
            q.save()
            return HttpResponseRedirect('/my_app/films/')
    else:
        form = FilmsForm()

    return render(request, 'my_app/add_film.html', {'form': form})


def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            q = Series(title=form.cleaned_data['title'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']), user = request.user)
            # q = Series(title=form.cleaned_data['title'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']))
            q.save()

            return HttpResponseRedirect('/my_app/series/')
    else:
        form = SeriesForm()

    return render(request, 'my_app/add_series.html', {'form': form})


def add_books(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            q = Books(title=form.cleaned_data['title'], author=form.cleaned_data['title'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']), user = request.user)
            # q = Books(title=form.cleaned_data['title'], author=form.cleaned_data['author'], comment=form.cleaned_data['comment'], img_url=get_img_url(form.cleaned_data['title']))
            q.save()

            return HttpResponseRedirect('/my_app/books/')
    else:
        form = BooksForm()

    return render(request, 'my_app/add_books.html', {'form': form})



def delete_film(request, film_id):
        if request.method == 'POST':
            film = Films.objects.get(pk=film_id)
            film.delete()
            return redirect('/my_app/films/')
        else:
            return HttpResponseRedirect('/my_app/films/')


def delete_watched_film(request, film_id):
    if request.method == 'POST':
        film = WatchedFilms.objects.get(pk=film_id)
        film.delete()
        return redirect('/my_app/watched_films/')
    else:
        return HttpResponseRedirect('/my_app/watched_films/')


def delete_series(request, series_id):
        if request.method == 'POST':
            series = Series.objects.get(pk=series_id)
            series.delete()
            return redirect('/my_app/series/')
        else:
            return HttpResponseRedirect('/my_app/series/')


def delete_watched_series(request, series_id):
    if request.method == 'POST':
        film = WatchedSeries.objects.get(pk=series_id)
        film.delete()
        return redirect('/my_app/watched_series/')
    else:
        return HttpResponseRedirect('/my_app/watched_series/')


def delete_books(request, book_id):
        if request.method == 'POST':
            books = Books.objects.get(pk=book_id)
            books.delete()
            return redirect('/my_app/books/')
        else:
            return HttpResponseRedirect('/my_app/books/')


def delete_readed_books(request, book_id):
    if request.method == 'POST':
        film = ReadedBooks.objects.get(pk=book_id)
        film.delete()
        return redirect('/my_app/readed_books/')
    else:
        return HttpResponseRedirect('/my_app/readed_books/')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/my_app/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})



