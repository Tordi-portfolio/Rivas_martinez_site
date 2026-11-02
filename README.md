# Rivas Martinez Cleaning Services - Django website

## Run it
```bash
cd rivas_martinez_site
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser   # this becomes your admin login
python manage.py runserver
```
- Website: http://127.0.0.1:8000/
- Admin message portal: http://127.0.0.1:8000/portal/ (staff accounts only; redirects to login)
- Built-in Django admin: http://127.0.0.1:8000/django-admin/

## Add more admins
Create a user in `/django-admin/` and tick **Staff status**. Non-staff accounts cannot sign in to the portal.

## Edit content
- Business details (phone, address, rating): `core/context.py`
- Services, FAQ, promises, testimonials: `core/content.py`
- Page text: `core/templates/core/*.html`; colors and fonts: `core/static/core/style.css`

## Before going live
Set env vars `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS=yourdomain.com`, run `python manage.py collectstatic`, and serve with gunicorn plus a static file server (WhiteNoise or nginx). Replace the sample testimonials with real ones from your clients.
"# Rivas_martinez_site" 
