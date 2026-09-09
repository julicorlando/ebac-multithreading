import asyncio

from django.http import JsonResponse


async def calculate_square(value, delay=0.5):
    """Simula uma operação assíncrona e retorna o quadrado do valor."""
    await asyncio.sleep(delay)
    return value * value


async def async_view(request):
    """View assíncrona usando async/await e asyncio.gather."""
    print("Iniciando view assíncrona...")

    results = await asyncio.gather(
        calculate_square(10),
        calculate_square(20),
        calculate_square(30),
    )

    total = sum(results)

    print(f"Resultados: {results}")
    print(f"Total: {total}")

    return JsonResponse(
        {
            "message": "View assíncrona executada com sucesso",
            "results": results,
            "total": total,
        }
    )
