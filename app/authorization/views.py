# -*- coding: utf-8 -*-
# Create your views here.

from django.template.loader import get_template #ищет и возвращает шаблон
from django.http import HttpResponse # основной НТТР ответ
from django.template import RequestContext # для передачи переменных в шаблон

#from portal.news.models import News, Comment # подключаем модели(таблицы бд0)
#from portal.news.forms import CommentForm # подключаем чт с формы
from django.http import HttpResponseRedirect #для переадресации
from django.core.urlresolvers import reverse
from django.contrib import auth #для работы с авторизацией-джанго
from django.template.response import TemplateResponse

#для регистрации
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
#forma
from authorization.forms import EditProfileForm

def custom_proc(request):

    return {
        'auth_form': AuthenticationForm(),
        }

#тестовая вьюха
def profile_show(request):
    if request.user.is_authenticated():
        user_name = request.user.username
    else:
        user_name = 'Гость'
    template = get_template("profile.html")
    context = RequestContext(request, {"user_name":user_name,})
    return HttpResponse(template.render(context))

def auth_show(request, template = 'index.html'):
    if request.POST:
        form = AuthenticationForm(request.POST)
    context = {}
    return render_to_response(template, context,
                context_instance=RequestContext(request, processors=[custom_proc]))

#редактирование профиля
def profile_edit(request):
    if request.method == 'POST':
        prof_edit_form = EditProfileForm(request.POST)
        if prof_edit_form.is_valid():
            username = prof_edit_form.cleaned_data['username']
            birth_year = prof_edit_form.cleaned_data['birth_year']
            gender = prof_edit_form.cleaned_data['gender']
            email = prof_edit_form.cleaned_data['email']
            town = prof_edit_form.cleaned_data['town']
            return HttpResponseRedirect('/profile/')
    else:
        prof_edit_form = EditProfileForm()
    template = 'profile_edit.html'
    context = {'prof_edit_form':prof_edit_form,}    
    return render_to_response(template, context,
                context_instance=RequestContext(request, processors=[custom_proc]))
#---------------
#регистрация
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/news/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html",{
        'form':form,   
    })
    
def login_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResonseRedirect("/account/loggedin")
    else:
        return HttpResponseRedirect("/account/invalid/")

