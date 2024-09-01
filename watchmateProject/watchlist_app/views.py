# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # This a function based view working with querysets

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#         }

#     return JsonResponse(data)
#     # #values function returns as a python dictionary"
#     # print(movies.values())
#     # return JsonResponse()

# def movie_details(request,pk):
#     movie = Movies.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description':movie.description,
#         'active': movie.active
#     }

#     return JsonResponse(data)