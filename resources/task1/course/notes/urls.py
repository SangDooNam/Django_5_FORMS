"""Notes URL Configuration."""
from django.urls import path

from notes.views import NotesBySection, NoteDetails, home, SearchResultsView, SectionList, SearchView, AddView, EditView

app_name = "notes"
urlpatterns = [
    path('', home, name="home"),
    path('sections/', SectionList.as_view(), name="sections"),
    path('sections/<section_name>/', NotesBySection.as_view(), name="by_section"),
    path('<int:note_id>/', NoteDetails.as_view(), name="details"),
    path('search/<str:search_term>/<str:select>/', SearchResultsView.as_view(), name="search_term"),
    path('search/', SearchView.as_view(), name='search'),
    path('add/', AddView.as_view(), name='add'),
    path('<int:note_id>/edit/', EditView.as_view(), name='edit')
]
