location /static/ {
        alias /home/app7/web/static/;
}

location /media/ {
        alias /home/app7/web/media/;
}
