from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'), #remember as_view is a function and you need to add the '()'
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),

    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('review', ReviewList.as_view(), name= 'review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
         ]