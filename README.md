# CODEMATRIX

Premium software-engineering agency website built with **Django + MySQL**, **Tailwind CSS**, custom CSS and **vanilla JavaScript**. Content (services, technologies, industries, case studies) is managed from the Django admin.

## Features
- 9 pages: Home, Services, AI & Data, Technologies, Industries, Our Work, Case Study detail, About, Contact (+ custom 404)
- **Our Work**: category filters, live search, "load more", detail page with gallery
- Contact form saved to MySQL, CSRF protected, honeypot spam trap, optional email notification
- Three.js hero matrix (2D canvas fallback), canvas neural network, animated architecture diagram, custom cursor
- Responsive (320px → 1920px), `prefers-reduced-motion` support, lazy-loaded images

## Tech stack
Python, Django 5, MySQL (via PyMySQL), Tailwind CSS (CDN), Vanilla JS, Three.js (home page only).

## Installation
```bash
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env         # macOS/Linux: cp .env.example .env
```
Generate a secret key and paste it into `.env`:
```bash
python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

## MySQL setup
```sql
CREATE DATABASE codematrix CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'codematrix_user'@'localhost' IDENTIFIED BY 'choose-a-strong-password';
GRANT ALL PRIVILEGES ON codematrix.* TO 'codematrix_user'@'localhost';
FLUSH PRIVILEGES;
```
Then set `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` in `.env`.
(For a quick test without MySQL set `DB_ENGINE=sqlite`.)

## Environment variables
See `.env.example`. Never commit `.env`. Leave `EMAIL_HOST` empty to print emails in the console; set `CONTACT_EMAIL` to receive inquiry notifications.

## Run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data        # SAMPLE demo content (not real clients)
python manage.py runserver
```
Site: http://127.0.0.1:8000/ — Admin: http://127.0.0.1:8000/admin/

Migrations are already included. If you change models, run `python manage.py makemigrations`.

## Managing content
In the admin, add a **Case Study**, choose its category and industry (they drive the filters), upload a featured image and gallery images. Untick *Is sample data* for real projects.

## Static files & production notes
- `python manage.py collectstatic` before deploying; serve `staticfiles/` and `media/` via your web server (or WhiteNoise).
- Set `DEBUG=False`, a strong `SECRET_KEY` and your domain in `ALLOWED_HOSTS`. HTTPS-only cookies/HSTS turn on automatically when `DEBUG=False`.
- Tailwind is loaded from the Play CDN for a build-free setup. For production, compile it with the Tailwind CLI (`tailwind.config.js` colours are in `static/js/tailwind.config.js`).
- The custom 404 page only appears when `DEBUG=False`.
- Run behind gunicorn/uvicorn + nginx.
