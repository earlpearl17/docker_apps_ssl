location /static/ {
	alias /home/app1/web/static/;
}

location /media/ {
        alias /home/app1/web/media/;
}
