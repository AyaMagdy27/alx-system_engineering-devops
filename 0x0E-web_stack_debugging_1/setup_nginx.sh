#!/bin/bash

# Update package list
apt-get update

# Install Nginx if not already installed
apt-get install -y nginx

# Create a simple HTML file to be served
cat <<EOL > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Nginx!</title>
</head>
<body>
    <h1>Success! The Nginx web server is installed and working!</h1>
</body>
</html>
EOL

# Set correct permissions for the HTML file
chmod 644 /var/www/html/index.html

# Ensure Nginx is configured to listen on port 80
if ! grep -q "listen 80;" /etc/nginx/sites-available/default; then
    sed -i 's/listen 80 default_server;/listen 80;/g' /etc/nginx/sites-available/default
fi

# Start Nginx using the nginx command
nginx -g 'daemon off;'

