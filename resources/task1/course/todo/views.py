"""Todo views."""
from typing import Any
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import LoginForm
from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate

from todo.models import todos


class LoginView(View):
    
    def get(self, request, todo_id):
        
        form = LoginForm()
        context = {
            'form' : form,
        }
        return render(request, "todo/login.html", context)
    
    def post(self, request, todo_id):
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            input_user = form.cleaned_data['user_name']
            input_password = form.cleaned_data['password']
            
            user = authenticate(username=input_user, password=input_password)
            
            if user is not None:
                
                n = len(todos)
                topic = todos[todo_id-1]['topic']
                text = todos[todo_id-1]['text']
                status = todos[todo_id-1]['status']
                previous = reverse('todo:details', args=[todo_id-1 if todo_id != 1 else todo_id])
                next = reverse('todo:details', args=[todo_id+1 if todo_id != n else todo_id])
                
                context = {
                    'todo_id': todo_id,
                    'topic': topic,
                    'text': text,
                    'status': status.capitalize(),
                    'previous': previous,
                    'next': next,
                }
                
                return render(request, "todo/details.html", context)
        
            else:
                
                login_fail = "Username or password are wrong."
                back = reverse('todo:details', args=[todo_id])
                context = {
                    'login_fail': login_fail,
                    'back': back,
                }
                return render(request, "todo/login_fail.html", {'login_fail': login_fail})
        else:
            
            return render(request, "todo/login.html", {'form': form})


