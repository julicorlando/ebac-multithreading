# Exercício EBAC - Django Templates e Admin

Neste exercício, o projeto passa a ter uma camada visual usando Django Templates e um modelo gerenciado pelo Django Admin.

## Implementado

- modelo `Post`;
- registro de `Post` no Django Admin;
- migration inicial;
- `base.html`;
- `index.html`;
- `post.html`;
- `detail.html`;
- `sidebar.html`;
- view de listagem e view de detalhe;
- testes das views e do registro no Admin.

> Observação: o enunciado cita modelos construídos em aulas anteriores, mas esses modelos não estavam presentes no repositório usado nos exercícios anteriores. Por isso foi adotado um modelo mínimo `Post`, coerente com os templates `post` e `detail` citados no exercício.

## Executar

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse:

- portfólio: `http://127.0.0.1:8000/home/`
- administração: `http://127.0.0.1:8000/admin/`

Para cadastrar conteúdo, entre no Admin e adicione registros em **Posts**.
