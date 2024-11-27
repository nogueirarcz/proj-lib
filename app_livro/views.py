from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_user.models import User
from app_livro.models import Livros

# Create your views here.
def home(request):

    if request.session.get('user'):

        user = User.objects.get(id = request.session['user'])

        livros = Livros.objects.filter(usuario = user)

        return render(request, 'home.html', {'livros': livros})

    else:

        return redirect('/auth/login/?status=2')
    
def ver_livro(request, id):

    if request.session.get('user'):

        livros = Livros.objects.get(id=id)

        if request.session.get('user') == livros.usuario.id:

            return render(request, 'ver_livro.html', {'livro': livros})
        else:

            return HttpResponse('Página indisponível')
    else:

        return redirect('/auth/login/?status=2')
        