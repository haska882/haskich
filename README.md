# haskich

Небольшой пример модели заказов на Python, SQLAlchemy 2 и SQLite.

## Что реализовано

- **User → Order**: связь один-ко-многим через `orders.user_id` и `relationship(..., back_populates=...)`.
- **Order ↔ Product**: связь многие-ко-многим через промежуточную таблицу `order_products`.
- В `seed.py` создаются два пользователя, три заказа и три товара. У Анны минимум два заказа; один товар входит в оба её заказа.
- Демонстрируется чтение: пользователь → заказы → товары, а также товар → заказы → пользователь.

## Запуск

Требуется Python 3.10 или новее.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
python seed.py
```

Скрипт каждый запуск пересоздаёт локальную базу `orders.db` и выводит связанные данные.

## Структура

- `models.py` — ORM-модели и таблица связи.
- `seed.py` — заполнение тестовыми данными и чтение связей.
- `requirements.txt` — зависимость SQLAlchemy.
