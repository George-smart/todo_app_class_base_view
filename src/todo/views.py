from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import TodoApp
from .forms import TodoForm, SignUpForm, UpdateTodoForm
from django.urls import reverse_lazy, reverse
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

    
def complete(request, pk):
    todos = TodoApp.objects.get(id=pk)
    if request.POST.get('checkbox') == 'clicked':
        todos.is_complete = True
    else:
        todos.is_complete = False
        
    todos.save()
    return redirect('todo:home')
    

class DeleteTodo(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = TodoApp
    template_name = 'delete.html'
    
    success_url = reverse_lazy('todo:home')
   

class UpdateTodo(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = TodoApp
    form_class = UpdateTodoForm
    template_name = 'update.html'
    
    success_url = reverse_lazy('todo:home')
    
    
    
 
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    
    success_url = reverse_lazy('login')