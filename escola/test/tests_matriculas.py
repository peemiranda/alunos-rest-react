# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from escola.models import Matricula, Aluno
#
#
# class CursosTestCase(APITestCase):
#
#     def setUp(self):
#         self.detail_url = lambda id_matricula: reverse('Matriculas-detail', args=[id_matricula])
#         self.list_url = reverse('Cursos-list')
#         self.matricula_1 = Matricula.objects.create(
#             aluno=Aluno.nome, curso='1', periodo='M'
#         )
#         self.matricula_2 = Matricula.objects.create(
#             aluno='casera', curso='2', periodo='V'
#         )
#         self.matricula_3 = Matricula.objects.create(
#             aluno='carcas', curso='3', periodo='N'
#         )
#         self.usuario = get_user_model().objects.create(username='username', password='admin')
#         self.client.force_login(self.usuario)
#
#     def test_requisicao_get_para_listar_matriculas(self):
#         """Teste para verificar a requisição GET para listar as matriculas"""
#         response = self.client.get(self.list_url)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#
#     def test_requisicao_post_para_criar_matriculas(self):
#         """Teste para verificar a requisição POST para criar uma matricula"""
#         data = {
#             'aluno': 'Sulamita',
#             'curso': 'Curso teste 4',
#             'peiodo': 'N'
#         }
#         response = self.client.post(self.list_url, data=data)
#         self.assertEquals(response.status_code, status.HTTP_201_CREATED)
#
#     def test_requisicao_delete_para_deletar_matricula(self):
#         """Teste para verificar a requisição DELETE não permitida para deletar uma matricula"""
#         response = self.client.delete(self.detail_url(1))
#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
#         response = self.client.get(self.list_url)
#         lista_alunos = response.json()
#         self.assertEquals(len(lista_alunos), 2)
#
#     def test_requisicao_put_para_atualizar_matricula(self):
#         """Teste para verificar a requisição PUT para atualizar uma matricula"""
#         data = {
#             'aluno': 'Paulo Adan',
#             'curso': 'Curso teste 1 atualizado',
#             'periodo': 'M'
#         }
#         response = self.client.put(self.detail_url(1), data=data)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#         # detail_url = reverse('Cursos-detail', args=[1])
