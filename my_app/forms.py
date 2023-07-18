from django import forms
from .models import Films, Series, Books, WatchedFilms, WatchedSeries, ReadedBooks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'comment']

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'comment']


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'comment']


class WatchedFilmsForm(forms.ModelForm):
    class Meta:
        model = WatchedFilms
        fields = ['title', 'comment']

class WatchedSeriesForm(forms.ModelForm):
    class Meta:
        model = WatchedSeries
        fields = ['title', 'comment']


class ReadedBooksForm(forms.ModelForm):
    class Meta:
        model = ReadedBooks
        fields = ['title', 'author', 'comment']



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})
        self.fields['password1'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})
        self.fields['password2'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']
