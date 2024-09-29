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

    # Criando e salvando o usuário
    user = User.objects.filter(email = email)

    # Verifica se nome ou email estão vazios
    if len(nome.strip()) == 0 or len(email.strip()) == 0:

        return redirect('/auth/cadastro/?status=1')

    # Verifica se já existe o usuário
    if len(user) > 0:

        return redirect('/auth/cadastro/?status=2')
    
    # Verifica tamanho da senha
    if len(senha) < 8:

        return redirect('/auth/cadastro/?status=3')
    
    try:

        user = User(nome = nome, senha = senha, email = email)
        user.save()

        return redirect('/auth/cadastro/?status=0')
    
    except:

        return redirect('/auth/cadastro/?status=4')
