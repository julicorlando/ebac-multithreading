# Exercício EBAC - Django Admin

Este exercício ativa e configura o Django Admin no projeto usado nas atividades anteriores.

## Objetivos

- disponibilizar o painel administrativo em `/admin/`;
- permitir a criação de um superusuário;
- permitir o gerenciamento de usuários e grupos pelo Django Admin;
- manter a rota `/home/` funcionando.

## Como executar

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Depois acesse:

- `http://127.0.0.1:8000/admin/`
- `http://127.0.0.1:8000/home/`

O enunciado não define novos modelos ou campos específicos para cadastro, então este exercício mantém os modelos existentes e configura corretamente o painel administrativo.
