# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.contrib import messages
import json

from .models import Posts


class MyForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['link', 'description']

@login_required
def show_post(request):

    # this gets all the posts, not just for the logged in user
    # posts = Posts.objects.all().order_by('order')

    # this gets just for the current user
    posts = Posts.objects.filter(user = request.user).order_by('order')
    
    context = {
        'posts':posts
    }
    return render(request, "posts/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "error")
    else:
        form = UserCreationForm()
    return render(request, 'posts/signup.html', {'form': form})


def delete(request, pk):
    Posts.objects.filter(pk=pk).delete()
    return redirect('show_post')
    # return render(request, 'posts/index.html')

def add_page(request):
    form = MyForm(request.POST or None)
    if form.is_valid():
        # commit=False is important for adding additional properties to savedForm before saving to database
        savedForm = form.save(commit=False)
        # this gets the maximum in the whole column, we just need the max for the current user
        # max_order_value = Posts.objects.all().aggregate(Max('order'))
        max_order_value = Posts.objects.filter(user = request.user).aggregate(Max('order'))
        if(max_order_value['order__max'] is not None):
            savedForm.order = max_order_value['order__max'] + 1
        print(request.user)
        savedForm.user = request.user

        print(savedForm.user)
        savedForm.save()
        return redirect ('show_post')
    
    return render(request, 'posts/add_page.html', {'form': form})
    # return redirect('/add_page')

def edit(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    form = MyForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('show_post')
    return render(request, 'posts/add_page.html', {'form':form})

@csrf_exempt
def sort(request):
    print(request)
    # response = request.POST.get('data')
    response = json.loads(request.body)
    # print(request.body)
    # print(response)
    idsArray = response['paramName']
    i = 0
    while i < len(idsArray):
        object = Posts.objects.get(pk=idsArray[i])
        print(object)
        object.order = i
        object.save()
        i += 1
    # item = Posts.objects.get(pk=idsArray[0])
    # print(item.title)
    return redirect('show_post')


