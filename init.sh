sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf /etc/gunicorn.d/test_hello
sudo ln -sf /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/test_django

#source /home/box/web/venv/bin/activate

#gunicorn3 -c /home/box/web/etc/gunicorn_hello.conf  hello:app
gunicorn3 -c /home/box/web/etc/gunicorn_django.conf  ask.wsgi:application

sudo /etc/init.d/nginx restart
