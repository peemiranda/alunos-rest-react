from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class AlunosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.detail_url = lambda id_aluno: reverse('Alunos-detail', args=[id_aluno])
        self.aluno_1 = Aluno.objects.create(
            nome='Pedro', rg='533845567', cpf='52509473875', data_nascimento='2004-12-31', celular='11957779332'
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Pedra', rg='533845561', cpf='52509473871', data_nascimento='2003-11-30', celular='11957779331'
        )
        self.aluno_3 = Aluno.objects.create(
            nome='Pedre', rg='533845562', cpf='52509473872', data_nascimento='2002-10-29', celular='11957779333'
        )
        self.usuario = get_user_model().objects.create(username='username', password='admin')
        self.client.force_login(self.usuario)

    def test_requisicao_get_para_listar_alunos(self):
        """
        Teste para verificar a requisição GET para listar os alunos
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_alunos(self):
        """Teste para verificar a requisição POST para criar um aluno"""
        data = {
            'nome': 'Gabriel Morishita',
            'rg': '123456789',
            'cpf': '39582647000',
            'data_nascimento': '2002-10-29',
            'celular': '1199321456'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delelte_para_deletar_aluno(self):
        """Teste para verificar a requisição DELETE para deletar um aluno"""
        response = self.client.delete(self.detail_url(1))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(self.list_url)
        lista_alunos = response.json()
        self.assertEquals(len(lista_alunos), 2)

    def test_requisicao_put_para_atualizar_aluno(self):
        """Teste para verificar a requisição PUT para atualizar um aluno"""
        data = {
            'nome': 'pedri',
            'rg': '533845560',
            'cpf': '52509473870',
            'data_nascimento': '2001-09-28',
            'celular': '11957779330'
        }
        response = self.client.put(self.detail_url(1), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
