import time


def LogMiddleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        execution_time = time.time() - start_time

        with open("logs.txt", "a", newline="\n", encoding="utf-8") as file:
            log = (
                f'Шлях: "{request.path}", метод запиту: "{request.method}", '
                f"час виконання запиту: {execution_time} секунди;\n"
            )
            file.write(log)
        return response

    return middleware
