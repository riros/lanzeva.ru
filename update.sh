#!/usr/bin/env bash
git pull
python3 manage.py collectstatic --noinput
python3 manage.py migrate
python manage.py thumbnail clear_delete_all
systemctl restart uwsgi-app@lanzeva
systemctl restart nginx
chown nginx:nginx -R ../lanzeva.ru/
