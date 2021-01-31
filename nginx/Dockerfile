FROM nginx:1.18.0

# Remove the default nginx.conf
# linking std out and err to the logs enables docker containers to ese
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf var/cache/apk/*


# put in our own water tracker conf file to the container's file
COPY water_tracker.conf /etc/nginx/conf.d/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
