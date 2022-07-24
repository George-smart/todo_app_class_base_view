from django import forms
from .models import TodoApp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['todo']

        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Add a todo'})
        }
        

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['todo']

        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Add a todo'})
        }

        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
