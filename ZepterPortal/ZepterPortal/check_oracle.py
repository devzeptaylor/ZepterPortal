from django.db import connections

class Command(BaseCommand):
    help = "Проверка подключения к Oracle базе данных"

    def handle(self, *args, **kwargs):
        try:
            # Используем соединение с Oracle
            with connections['oracle'].cursor() as cursor:
                cursor.execute("SELECT * FROM v$version")
                result = cursor.fetchone()
                self.stdout.write(self.style.SUCCESS(f"Подключение успешно! Версия Oracle: {result[0]}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка подключения: {e}"))