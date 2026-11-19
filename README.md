# HotelFlow

Інформаційна система управління готелем «Карпатська зоря» (PMS): бронювання, заселення, рахунки, прибирання номерів, звіти.

Стек: Python 3.12 + Django REST Framework, React + TypeScript (Vite), PostgreSQL 16, Redis, Docker.

## Швидкий старт (Docker)

Потрібно: Git, Docker Desktop.

```bash
git clone <URL цього репозиторію> hotelflow
cd hotelflow
cp .env.example .env
docker compose up --build
```

Після запуску:

| Сервіс | Адреса |
|---|---|
| Веб-інтерфейс | http://localhost:5173 |
| API (перевірка) | http://localhost:8000/api/v1/health/ |
| Список номерів | http://localhost:8000/api/v1/rooms/ |
| Адмінка Django | http://localhost:8000/admin/ |

Під час першого запуску автоматично виконуються міграції і створюються 85 тестових номерів (`seed_rooms`).

Створити адміністратора:

```bash
docker compose exec backend python manage.py createsuperuser
```

## Запуск без Docker

Backend (база SQLite створиться автоматично):

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_rooms
python manage.py runserver
```

Frontend (в іншому терміналі, потрібен Node.js 20+):

```bash
cd frontend
npm install
npm run dev
```

## Структура

```
backend/    Django-проєкт (hotelflow) і застосунок rooms
frontend/   React + TypeScript (Vite)
docker-compose.yml
.env.example
```

## Правила роботи

- Гілки: `feature/HTF-<номер>-короткий-опис` (номер задачі з Jira).
- Коміти: `HTF-<номер>: що зроблено`.
- Кожна зміна йде через merge request і код-рев'ю.
