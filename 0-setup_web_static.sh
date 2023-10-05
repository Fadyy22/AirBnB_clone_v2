#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo 'Hello World!' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;
        location /redirect_me {
                 return 301 http://google.com;
        }

        error_page 404 /404.html;

        location = /404.html {
                root /usr/share/nginx/html;
                internal;
        }

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }
}" > /etc/nginx/sites-available/default'
sudo service nginx restart
