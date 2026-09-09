# Multithreading Web Scraper

Projeto desenvolvido durante o curso da EBAC para praticar conceitos de Python avançado, web scraping e concorrência.

## Autor

Júlio Orlando

## Objetivo

O projeto realiza a coleta de informações de filmes e compara o tempo de execução entre:

- execução sequencial;
- execução com múltiplas threads usando `ThreadPoolExecutor`.

## Tecnologias utilizadas

- Python 3
- requests
- BeautifulSoup
- concurrent.futures
- CSV

## Como executar

Instale as dependências:

```bash
python -m pip install requests beautifulsoup4
```

Depois execute:

```bash
python multithreading.py
```

## Saída

O programa gera arquivos CSV com os dados coletados e exibe no terminal o tempo de execução das abordagens sequencial e multithread.

## Exercício Git/GitHub

Este repositório também faz parte do exercício de Git e GitHub da EBAC, utilizando:

- repositório Git;
- branch de desenvolvimento;
- commits;
- push;
- Pull Request.
