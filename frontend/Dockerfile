# Use the official Nginx image as a base
FROM nginx:alpine

# Copy your static files (e.g., HTML, CSS, JS) to the Nginx root directory
COPY ./index.html /usr/share/nginx/html/index.html

# Copy the background image to the Nginx root directory
COPY ./background.avif /usr/share/nginx/html/background.avif

# Expose the port Nginx will run on
EXPOSE 80
