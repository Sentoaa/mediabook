from django.db import models
from django.contrib.auth.models import User



class Films(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"


class WatchedFilms(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"


class Series(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"


class WatchedSeries(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"


class Books(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    author = models.CharField(max_length=100)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"


class ReadedBooks(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000, default='', blank=True)
    author = models.CharField(max_length=100)
    comment = models.TextField(default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.comment}"



