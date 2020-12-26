#ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#/etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo -s /etc/init.d/nginx restart
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/gunicorn-django.py
sudo gunicorn -c /etc/gunicorn.d/gunicorn-django.py ask.wsgi:application
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py


