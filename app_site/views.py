from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'index.html')

def enviar_mensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        # Usando send_mail:
        send_mail(
            'Mensagem Site',
            f'Mensagem de: {nome}\nEmail: {email}\nMensagem: {mensagem}',
            {email}, 
            ['arthurtmo@usp.br'],  
            fail_silently=True,
        )
        
        # Após enviar o e-mail, você pode redirecionar o usuário para uma página de confirmação
        return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html') 
