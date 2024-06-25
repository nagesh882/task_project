from django.urls import path
from api import views



urlpatterns = [
    path('get-data/', views.user_view),
]
