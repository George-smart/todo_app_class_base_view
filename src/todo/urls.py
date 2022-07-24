from django.urls import path
from .views import HomeView, SignUp, complete, DeleteTodo, UpdateTodo

app_name = "todo"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignUp.as_view(), name='signup'),
    path('complete/<int:pk>', complete, name='complete'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete'),
    path('update/<int:pk>', UpdateTodo.as_view(), name='update'),
]
