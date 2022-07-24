from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import TodoApp
from .forms import TodoForm, SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = TodoApp
    form_class = TodoForm
    template_name = 'index.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        todos = TodoApp.objects.filter(user=self.request.user)
        context['todos'] = todos
        
        return context

    
        
    
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    
    success_url = reverse_lazy('login')