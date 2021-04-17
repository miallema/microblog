ps aux |grep gunicorn |grep microblog:app | awk '{ print $2 }' | xargs kill
gunicorn -b localhost:8000 -w 1 microblog:app &


