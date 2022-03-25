location /static/ {
        alias /home/app4/web/static/;
}

location /media/ {
        alias /home/app4/web/media/;
}
