from django.urls import path
from .views import HomeView, SignUp

app_name = "todo"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignUp.as_view(), name='signup'),
]
