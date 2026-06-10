from datetime import date

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        try:
            return date.fromisoformat(value)
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD.")

    def to_url(self, value):
        return value.__str__()