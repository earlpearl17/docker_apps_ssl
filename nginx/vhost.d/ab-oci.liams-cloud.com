location /static/ {
        alias /home/app3/web/static/;
}

location /media/ {
	alias /home/app3/web/media/;
}

