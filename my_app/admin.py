from django.contrib import admin

from .models import Films
from .models import WatchedFilms
from .models import Series
from .models import WatchedSeries
from .models import Books
from .models import ReadedBooks

admin.site.register(Films)
admin.site.register(WatchedFilms)
admin.site.register(Series)
admin.site.register(WatchedSeries)
admin.site.register(Books)
admin.site.register(ReadedBooks)
