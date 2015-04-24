web: gunicorn manage:app -w 3
celery: celery -A tasks worker -c 3 -B
