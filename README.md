# Overview

Aplicação feita em Python 3.6 com o auxilio do framework Django, visando usar também, APIs feitas com Django Rest Framework.

### Motivação
Deseja-se achar a rota, entre dois pontos de uma cidade, com o menor custo.

### Metodologia
Foram criadas duas APIs para solucionar o problema: 

1. API `saveMap` que recebe uma malha lógica (exemplo a seguir) e salva persistentemente. Na malha é encontrado informações como o nome do mapa, um ponto de origem, um ponto de destino e sua distância.

```json
{
    "mapName": "SP",
    "route": [
                ["A","B",10],
                ["B","D",15],
                ["C","E",24],
                ["E","F",1]
             ]   
}
```

2. API `shorterDistance` calcula a rota de menor custo entre dois pontos enviados na requisição da API. 

```json
{
    "mapName": "SP",
    "start": "A",
    "end": "D",
    "autonomy": 10,
    "liters": 2.50
}
```
### Como usar

Depois de clonado o projeto inicie a aplicação:
`$python manage.py runserver`

Execute uma requisição para as URL (Ambos utilizam método POST):

http://127.0.0.1:8000/api/saveMap/

ou 

http://127.0.0.1:8000/api/shorterDistance/

Adicione no Body da requisição um JSON com as seguintes informações:

Para requisição em `api/saveMap/`:
```
{
    "mapName": "SP", //nome do mapa que deseja ser salvo
    "route": //uma lista de distancia, sendo na ordem Ponto origem, Ponto destino e distância
    [ 
        ["A","B",10],
        ["B","D",15],
        ["A","C",20],
        ["C","D",30],
        ["B","E",50],
        ["D","E",30]
    ]   
}
```

Para requisição em `api/shorterDistance/`:
```
{
    "mapName": "SP", //nome do mapa que deseja ser feita a busca
    "start": "A", //O ponto inicial (origem)
    "end": "D", //O ponto final (destino)
    "autonomy": 10, //A autonomia do automóvel
    "liters": 2.50 //O valor do litro de combustível
}
```

### Retorno (Response)
* Para a requisição em `api/saveMap/`:

Retornará `True` se o mapa for salvo com sucesso, e um erro caso contrário.

* Para a requisição em `api/shorterDistance/`:

Retornará um JSON com o caminho e o custo no formato a seguir.
```json
{ 
  "path": ["A", "B", "D"],    
  "cost": 6.25
}
```