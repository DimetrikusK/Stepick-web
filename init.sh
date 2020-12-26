#ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#/etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
<<<<<<< HEAD
ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
gunicorn -c /home/box/web/etc/gunicorn-wsgi.conf hello:app
gunicorn -c /home/box/web/etc/gunicorn-django.conf asl.wsgi:aplication
#sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

#sudo /etc/init.d/gunicorn restart
=======
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/shit.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/shit
gunicorn -b :8080 hello:app
>>>>>>> 8c7649973076d0663cf048c1f510efdf5b0bdee4
