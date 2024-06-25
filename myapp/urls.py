from django.urls import path
from myapp import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name="sign_out")
]
