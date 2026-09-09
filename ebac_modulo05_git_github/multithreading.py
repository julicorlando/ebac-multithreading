import csv
import time
import random
import concurrent.futures
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://havokkmorands.github.io/"
POPULAR_MOVIES_URL = "https://havokkmorands.github.io/movie-catalog/"
MAX_THREADS = 10

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def get_movie_links():
    """Obtém os links dos filmes disponíveis no catálogo."""
    response = requests.get(
        POPULAR_MOVIES_URL,
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    container = soup.find(
        "section",
        attrs={"data-testid": "movies-list"},
    )

    if container is None:
        raise RuntimeError("Container principal de filmes não encontrado.")

    movie_items = container.find_all(
        "article",
        attrs={"data-testid": "movie-item"},
    )

    movie_links = []

    for movie in movie_items:
        link_tag = movie.find(
            "a",
            attrs={"data-testid": "movie-link"},
            href=True,
        )

        if link_tag:
            movie_links.append(
                urljoin(BASE_URL, link_tag["href"])
            )

    return movie_links


def extract_movie_details(movie_link):
    """Extrai título, lançamento, nota e sinopse de um filme."""
    time.sleep(random.uniform(0, 0.2))

    response = requests.get(
        movie_link,
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    detail_container = soup.find(
        "section",
        attrs={"data-testid": "movie-detail"},
    )

    if detail_container is None:
        return None

    title_tag = detail_container.find(
        attrs={"data-testid": "movie-title"}
    )
    release_tag = detail_container.find(
        attrs={"data-testid": "movie-release"}
    )
    rating_tag = detail_container.find(
        attrs={"data-testid": "movie-rating"}
    )
    synopsis_tag = detail_container.find(
        attrs={"data-testid": "movie-synopsis"}
    )

    title = (
        title_tag.get_text(strip=True)
        if title_tag else None
    )
    release_date = (
        release_tag.get_text(strip=True)
        .replace("Lançamento:", "")
        .strip()
        if release_tag else None
    )
    rating = (
        rating_tag.get_text(strip=True)
        .replace("Nota:", "")
        .strip()
        if rating_tag else None
    )
    synopsis = (
        synopsis_tag.get_text(strip=True)
        .replace("Sinopse:", "")
        .strip()
        if synopsis_tag else None
    )

    if all([title, release_date, rating, synopsis]):
        return [title, release_date, rating, synopsis]

    return None


def save_csv(filename, movies):
    """Salva os dados coletados em CSV."""
    with open(
        filename,
        mode="w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            ["title", "release_date", "rating", "synopsis"]
        )
        writer.writerows(movies)


def run_sequential(movie_links):
    """Executa a coleta usando apenas uma thread."""
    start_time = time.perf_counter()

    movies = []

    for movie_link in movie_links:
        movie = extract_movie_details(movie_link)

        if movie:
            movies.append(movie)

    elapsed_time = time.perf_counter() - start_time

    save_csv("movies_sequential.csv", movies)

    return elapsed_time, movies


def run_multithreading(movie_links):
    """Executa a coleta usando múltiplas threads."""
    start_time = time.perf_counter()

    workers = min(MAX_THREADS, len(movie_links))

    if workers == 0:
        return 0.0, []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=workers
    ) as executor:
        results = list(
            executor.map(
                extract_movie_details,
                movie_links,
            )
        )

    movies = [
        movie
        for movie in results
        if movie is not None
    ]

    elapsed_time = time.perf_counter() - start_time

    save_csv("movies_multithreading.csv", movies)

    return elapsed_time, movies


def main():
    movie_links = get_movie_links()

    print(f"Filmes encontrados: {len(movie_links)}")
    print("-" * 50)

    sequential_time, sequential_movies = run_sequential(
        movie_links
    )

    print(
        "Execução sequencial concluída:"
        f" {len(sequential_movies)} filmes"
    )
    print(
        f"Tempo sequencial: {sequential_time:.4f} segundos"
    )

    print("-" * 50)

    threaded_time, threaded_movies = run_multithreading(
        movie_links
    )

    print(
        "Execução com multithreading concluída:"
        f" {len(threaded_movies)} filmes"
    )
    print(
        f"Tempo com multithreading:"
        f" {threaded_time:.4f} segundos"
    )

    print("-" * 50)

    if threaded_time > 0:
        speedup = sequential_time / threaded_time
        print(f"Speedup aproximado: {speedup:.2f}x")

    print(
        "\nArquivos gerados:"
        "\n- movies_sequential.csv"
        "\n- movies_multithreading.csv"
    )


if __name__ == "__main__":
    main()
