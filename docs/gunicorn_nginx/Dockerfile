# start from an official image
FROM nginx_gunicorn

# arbitrary location choice: you can change the directory
# RUN mkdir -p /opt/services/djangoapp/src
# WORKDIR /opt/services/djangoapp/src
WORKDIR /app

# install our two dependencies
# RUN pip install gunicorn django

# copy our project code
# COPY . /opt/services/djangoapp/src

# expose the port 8050
EXPOSE 8055

# define the default command to run when starting the container
#CMD ["gunicorn", "--chdir", "hello", "--bind", ":8000", "hello.wsgi:application"]
CMD ["/usr/local/bin/gunicorn", "--bind", ":8000", "web_application:application"]
#CMD /usr/local/bin/gunicorn --bind :8055 /app/web_application:application

# Run docker using following command
# docker run -it -d -p 8085:8000 nginx_gunicorn
# Once running check http://127.0.0.1:8055
# you will be able to see web page with message as "Hello my friend!, using Gunicorn WSGI"