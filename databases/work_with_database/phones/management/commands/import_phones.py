import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # Пропускаем заголовок
            next(phone_reader)

            imported_count = 0

            for line in phone_reader:
                # Убираем пустые элементы в конце строки (из‑за ; в конце)
                line = [item.strip() for item in line if item.strip()]

                # Проверяем, что в строке достаточно данных (5 полей без id)
                if len(line) < 5:
                    self.stderr.write(f'Пропущена строка с недостаточным количеством данных: {line}')
                    continue

                # Извлекаем данные с учётом реального порядка колонок в CSV
                name = line[1]  # второй столбец
                image = line[2]  # третий столбец
                price = float(line[3])  # четвёртый столбец
                release_date = line[4]  # пятый столбец
                lte_exists = line[5].lower() in ['true', '1', 'yes']  # шестой столбец

                # Создаём slug на основе названия
                slug = slugify(name.replace(' ', '-'))

                # Создаём объект модели и сохраняем в БД
                phone = Phone(
                    name=name,
            price=price,
            image=image,
            release_date=release_date,
            lte_exists=lte_exists,
            slug=slug
        )
                phone.save()
                imported_count += 1

        # Выводим итоговое сообщение
        self.stdout.write(
            self.style.SUCCESS(f'Успешно импортировано {imported_count} телефонов')
        )
