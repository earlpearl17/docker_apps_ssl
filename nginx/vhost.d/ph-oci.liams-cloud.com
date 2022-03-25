location /static/ {
        alias /home/app5/web/static/;
}

location /media/ {
        alias /home/app5/web/media/;
}
