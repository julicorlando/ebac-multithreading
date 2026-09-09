# Exercício EBAC - Django Async View

Projeto criado para praticar suporte assíncrono no Django com `async def`, `await` e recursos assíncronos do Python.

## Objetivo

Criar uma view assíncrona, executar operações com `await` e retornar o resultado de uma requisição GET.

## Rota

`http://127.0.0.1:8000/async/`

## Como executar

```bash
python -m pip install -r requirements.txt
python manage.py runserver
```

Depois acesse:

`http://127.0.0.1:8000/async/`

Resposta esperada:

```json
{
  "message": "View assíncrona executada com sucesso",
  "results": [100, 400, 900],
  "total": 1400
}
```

No terminal também serão exibidos o início da execução, os resultados e o total.

## Testes

```bash
pytest
```

O teste utiliza `AsyncClient` para validar a view assíncrona.
