# infoWebServer

A simple webserver for showing information about SpaceX-Launch-Bot. Written in Python+Flask using uWSGI to host, and using NGINX as a reverse proxy. Currently just parses the bots log file into HTML and then serves it over HTTP

See [here](https://www.nginx.com/resources/glossary/reverse-proxy-server/) for why NGINX is used

This allows me to easily see what is happening with the bot without having to SSH into my server

It currently does not require authentication to view as nothing personal, private or important is logged

Read `../SETUP.md` to install this correctly
