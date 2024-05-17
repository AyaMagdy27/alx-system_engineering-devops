FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
RUN echo "<!DOCTYPE html><html><head><title>Welcome to Nginx!</title></head><body><h1>Success! The Nginx web server is installed and working!</h1></body></html>" > /var/www/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
