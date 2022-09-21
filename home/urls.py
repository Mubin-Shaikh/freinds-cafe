# HOME APP URLS

from django.urls import path
from . import views
urlpatterns = [
    path("", views.menus, name="menus"),
    path("breakfast", views.breakfast, name="breakfast"),
    path("drinks", views.drinks, name="drinks"),
    path("reservations", views.reservations, name="reservations"),
    path("delivery", views.delivery, name="delivery"),
    path("ourstory", views.ourstory, name="ourstory"),
]
