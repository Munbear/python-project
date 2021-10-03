from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
  # signup 으로 POST 요청이 왔을때, 새로운 유저를 만드는 절차를 밟는다
  if request.method == 'POST':
    if request.POST['password'] == request.POST['confirm']:
      user = User.objects.create.user(username=request.POST['username'])
