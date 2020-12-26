#ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#/etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo -s /etc/init.d/nginx restart
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo -s ln -sf /home/box/web/etc/gunicorn-django.conf  /etc/gunicorn.d/gunicorn-django.conf
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py


