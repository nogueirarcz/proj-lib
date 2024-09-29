from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect

# Create your views here.
def login(request):

    return HttpResponse('login')


def cadastro(request):

    return render(request, 'cadastro.html')

def validar_cadastro(request):

    nome = request.POST.get('nome')

    email = request.POST.get('email')

    senha = request.POST.get('senha')

    # Criando e salvando o usuário (modelo de teste)

    user = User.objects.filter(email = email)
    if len(user > 0):

        return redirect('/auth/login/')
    
    try:

        user = User(nome = nome, senha = senha, email = email)
        user.save()

        return redirect('/auth/login/')
    
    except:

        return redirect('/auth/cadastro/')
