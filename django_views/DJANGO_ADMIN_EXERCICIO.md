# Exercício EBAC - Django Admin

Este exercício ativa e configura o Django Admin no projeto usado nas atividades anteriores.

## Objetivos

- disponibilizar o painel administrativo em `/admin/`;
- permitir a criação de superusuário;
- permitir o gerenciamento de usuários e grupos pelo Django Admin;
- manter a aplicação existente funcionando normalmente.

## Como executar

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois acesse:

`http://127.0.0.1:8000/admin/`

A rota anterior continua disponível em:

`http://127.0.0.1:8000/home/`
