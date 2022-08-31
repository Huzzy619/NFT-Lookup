from django.urls import path

from . import views as calendar_views

urlpatterns = [
    
    
    path('search-drops', calendar_views.search_drops_view, name='search-drops'),
    path('search-drops-date', calendar_views.search_by_date, name='search-drops-date'),






    path('calendar', calendar_views.limited_drops,  name='calendar'),
    path('calendar/drops/<day>', calendar_views.all_drops_by_days,  name='calendar-days'),

    path('add-calendar', calendar_views.add_calendar, name='add_calendar'),
]

