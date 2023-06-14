from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Favorite

import requests
# Create your views here.


class FavoriteList(APIView):
    def get(self, request, client_id):
        favorites = Favorite.objects.filter(client_id=client_id)
        # Realize o tratamento dos dados, se necessário
        # ...

        return Response("Lista de favoritos do cliente")

class FavoriteAdd(APIView):
    def post(self, request, client_id, produto_id):
        # Realize a chamada à API "Produto" para obter informações do produto
        produto_url = f"http://api-produto.com/produtos/{produto_id}"
        response = requests.get(produto_url)
        if response.status_code == 200:
            produto_data = response.json()

            # Salve os dados na tabela de favoritos
            favorite = Favorite(client_id=client_id, produto_id=produto_id)
            favorite.save()

            return Response("Favorito adicionado com sucesso")
        else:
            return Response("Falha ao adicionar favorito", status=response.status_code)
