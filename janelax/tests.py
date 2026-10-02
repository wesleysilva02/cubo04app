from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import DadosUsuario


class DadosUsuarioViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='123456')

    def test_form_salva_dados_do_usuario(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('index'),
            {
                'nome': 'Maria Silva',
                'email': 'maria@email.com',
                'telefone': '11999999999',
                'idade': '28',
                'curso': 'Django',
                'observacoes': 'Quero aprender mais sobre o projeto.'
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('boas_vindas'))
        self.assertContains(response, 'Maria Silva')
        self.assertContains(response, 'Boas-vindas')
        self.assertTrue(DadosUsuario.objects.filter(nome='Maria Silva').exists())
        usuario = DadosUsuario.objects.get(nome='Maria Silva')
        self.assertEqual(usuario.email, 'maria@email.com')
        self.assertEqual(usuario.curso, 'Django')

    def test_editar_usuario(self):
        self.client.force_login(self.user)

        usuario = DadosUsuario.objects.create(
            nome='Joao',
            email='joao@email.com',
            telefone='11999999999',
            idade=20,
            curso='Python',
            observacoes='Teste'
        )

        response = self.client.post(
            reverse('editar_usuario', args=[usuario.pk]),
            {
                'nome': 'Joao Atualizado',
                'email': 'joao.novo@email.com',
                'telefone': '11888888888',
                'idade': '22',
                'curso': 'Django',
                'observacoes': 'Atualizado'
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('listar_usuarios'))
        usuario.refresh_from_db()
        self.assertEqual(usuario.nome, 'Joao Atualizado')
        self.assertEqual(usuario.curso, 'Django')

    def test_excluir_usuario(self):
        self.client.force_login(self.user)

        usuario = DadosUsuario.objects.create(
            nome='Ana',
            email='ana@email.com',
            telefone='11777777777',
            idade=25,
            curso='JavaScript',
            observacoes='Excluir'
        )

        response = self.client.post(
            reverse('excluir_usuario', args=[usuario.pk]),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('listar_usuarios'))
        self.assertFalse(DadosUsuario.objects.filter(pk=usuario.pk).exists())

    def test_listar_usuarios_exige_login(self):
        response = self.client.get(reverse('listar_usuarios'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_cadastrar_usuario_na_tela_de_login(self):
        response = self.client.post(
            reverse('cadastrar_usuario'),
            {
                'username': 'novo_usuario',
                'password1': 'Senha@123',
                'password2': 'Senha@123',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(username='novo_usuario').exists())
        self.assertRedirects(response, reverse('listar_usuarios'))

    def test_login_com_sucesso(self):
        response = self.client.post(
            reverse('login'),
            {'username': self.user.username, 'password': '123456'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('listar_usuarios'))
