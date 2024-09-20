from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS
from rest_framework.routers import DefaultRouter #import Default router first
#Version 18, video Viewsets and Routers. Define router first
# 

router = DefaultRouter() 
router.register('stream', StreamPlatformVS, basename='streamplatform')



urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'), #remember as_view is a function and you need to add the '()'
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review', ReviewList.as_view(), name= 'review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review', ReviewList.as_view(), name = 'review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),
        
     ]