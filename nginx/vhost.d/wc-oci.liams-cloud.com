location /static/ {
        alias /home/app2/web/static/;
}

location /media/ {
        alias /home/app2/web/media/;
}


