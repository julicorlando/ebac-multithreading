# Exercício EBAC - Django Views

Autor: Júlio Orlando

Este projeto pratica Django Views, URLs, testes com PyTest e fluxo Git/GitHub.

## Funcionalidade

A rota:

`http://127.0.0.1:8000/home/`

retorna:

`Hello World`

## Instalação

```bash
python -m pip install -r requirements.txt
```

## Executar

```bash
python manage.py runserver
```

Depois acesse `http://127.0.0.1:8000/home/`.

## Testes

```bash
pytest
```

O teste valida o status HTTP 200 e o conteúdo `Hello World`.
