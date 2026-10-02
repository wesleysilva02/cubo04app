from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render

from .models import DadosUsuario


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = UserCreationForm()
        return context


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_usuarios')
    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/login.html',
        {
            'form': AuthenticationForm(),
            'register_form': form,
            'is_register': True,
        },
    )


@login_required
def index(request):
    context = {
        'NOME_USUARIO': 'Usuário',
        'curso': 'Django',
        'mensagem': '',
    }

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        idade = request.POST.get('idade', '0').strip()
        curso = request.POST.get('curso', '').strip()
        observacoes = request.POST.get('observacoes', '').strip()

        if nome and email and curso:
            DadosUsuario.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                idade=int(idade or 0),
                curso=curso,
                observacoes=observacoes,
            )
            request.session['nome_usuario'] = nome
            request.session['curso'] = curso
            return redirect('boas_vindas')

    return render(request, 'janelax/index.html', context)


@login_required
def boas_vindas(request):
    nome_usuario = request.session.get('nome_usuario', 'Usuário')
    curso = request.session.get('curso', 'Django')
    return render(
        request,
        'janelax/boas_vindas.html',
        {'nome_usuario': nome_usuario, 'curso': curso},
    )


@login_required
def listar_usuarios(request):
    usuarios = DadosUsuario.objects.all().order_by('-criado_em')
    return render(request, 'janelax/listar_usuarios.html', {'usuarios': usuarios})


@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(DadosUsuario, pk=usuario_id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome', usuario.nome).strip()
        usuario.email = request.POST.get('email', usuario.email).strip()
        usuario.telefone = request.POST.get('telefone', usuario.telefone).strip()
        usuario.idade = int(request.POST.get('idade', usuario.idade) or 0)
        usuario.curso = request.POST.get('curso', usuario.curso).strip()
        usuario.observacoes = request.POST.get('observacoes', usuario.observacoes or '').strip()
        usuario.save()
        return redirect('listar_usuarios')

    return render(request, 'janelax/editar_usuario.html', {'usuario': usuario})


@login_required
def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(DadosUsuario, pk=usuario_id)

    if request.method == 'POST':
        usuario.delete()

    return redirect('listar_usuarios')


@login_required
def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(DadosUsuario, pk=usuario_id)
    return render(request, 'janelax/detalhe_usuario.html', {'usuario': usuario})
