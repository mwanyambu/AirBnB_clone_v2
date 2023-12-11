#!/usr/bin/env bash
#script sets up web servers for deployment of web_static
if ! command -v nginx &> /dev/null;
then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Best School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i "38i\\\tlocation /hnbn_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
