# Exercício EBAC - Django Templates e Admin

Neste exercício, o projeto dá continuidade à atividade anterior do Django Admin e adiciona a camada visual usando Django Templates.

## Implementado

- modelo `Post` herdado da correção anterior;
- campo `slug` único e geração automática a partir do título;
- `prepopulated_fields` no Django Admin para preencher o slug ao digitar o título;
- campo `published` para controlar quais posts aparecem no site;
- registro de `Post` no Django Admin;
- migration inicial compatível com todos os campos do modelo;
- `base.html`;
- `index.html`;
- `post.html`;
- `detail.html`;
- `sidebar.html`;
- view de listagem exibindo apenas posts publicados;
- view de detalhe impedindo acesso a posts não publicados;
- testes das views, do slug e do registro no Admin;
- workflow de CI herdado da atividade anterior para validar migrations, Django check e testes.

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

Para cadastrar conteúdo, entre no Admin e adicione registros em **Posts**. Ao preencher o título, o campo slug é sugerido automaticamente. Apenas posts marcados como publicados são exibidos no site.
