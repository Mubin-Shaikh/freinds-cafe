# CAFEHOUSE PROJECT URLS

from django.contrib import admin
from django.urls import path, include

# changing django admin text manually 
admin.site.site_header = "Central-Perk-Cafe Admin"
admin.site.site_title = "Central-Perk-Cafe Admin Portal"
admin.site.index_title = "Welcome to Central-Perk-Cafe Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
]
