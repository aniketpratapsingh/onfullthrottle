from django.urls import path

from .views import SearchView

from . import views
app_name = "finterapp"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('search/', SearchView.as_view()),
    path('',views.index, name='index')
]