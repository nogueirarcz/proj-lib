from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_user.models import User

# Create your views here.
def home(request):

    if request.session.get('user'):

        user = User.objects.get(id = request.session['user']).nome

        return HttpResponse(f'Bem-vindo(a) {user}')

    else:

        return redirect('/auth/login/?status=2')
    