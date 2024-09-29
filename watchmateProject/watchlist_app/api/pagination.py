from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size= 7
    page_query_param = 'p' # Name of the string to identify page number. Default is page.
    page_size_query_param = 'size' #It allows client to dictate size of results, ex: http://127.0.0.1:8000/watch/list2/?size=10 also p=last default takes it to end page.
    max_page_size = 50 #allows you to limit the "page_size_query_param" attribute
    last_page_strings = 'end' #p=last default takes it to end page.

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10 #Optional
    limit_query_param = 'limit' #Optional
    offset_query_param = 'start' #Optional

class WatchListCPagination(CursorPagination):
    page_size = 5 
    ordering = 'created' # for ordering ascending or descending. Optional, -created is the default. 
    cursor_query_param = 'record'
    #Cursor for contract to force reader to go via every page.