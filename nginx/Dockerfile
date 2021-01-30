FROM nginx:1.18.0

# put in our own water tracker conf file to the container's file
COPY water_tracker.conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
