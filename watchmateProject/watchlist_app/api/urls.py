from django.urls import path, include
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'), #remember as_view is a function and you need to add the '()'
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]