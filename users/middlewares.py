from django.http import HttpResponseBadRequest


class WorkAgeMiddleware:
    def __init__(self, get_response):
        # Инициализация middleware
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, что запрос на страницу регистрации с методом POST
        if request.path == '/register/' and request.method == 'POST':
            try:
                # Получаем и проверяем количество лет работы
                work_years = int(request.POST.get('work_years', 0))
            except ValueError:
                # Если данные некорректны, возвращаем ошибку 400
                return HttpResponseBadRequest("Некорректные данные для 'work_years'")

            # Присваиваем зарплату в зависимости от количества лет работы
            if 0 < work_years <= 2:
                request.salary = 30000
            elif 3 <= work_years <= 5:
                request.salary = 50000
            elif work_years >= 6:
                request.salary = 70000
            else:
                # Если количество лет работы не подходит, ошибка
                return HttpResponseBadRequest("Некорректное количество лет работы")

        # Проверка GET-запроса на /register/ (необходимо ли это?)
        elif request.path == '/register/' and request.method == 'GET':
            # Можно оставить эту строку, если нужна дополнительная информация для GET-запросов
            setattr(request, 'club', 'Ошибка сервера')

        # Далее передаем запрос дальше по цепочке middleware
        response = self.get_response(request)
        return response

