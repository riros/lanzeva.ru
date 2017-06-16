#!/usr/bin/env bash
git pull
python3 manage.py collectstatic --noinput
python3 manage.py migrate
#python manage.py thumbnail clear_delete_all
#systemctl restart uwsgi-app@lanzeva
systemctl restart uwsgi
systemctl restart nginx
chown www-data:www-data -R ../lanzeva.ru/
