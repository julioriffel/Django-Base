FROM python:3.9

# set work directory
WORKDIR /home/app/web

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /home/app/web/
RUN pip install pipenv && pipenv install --system

# copy our project code
COPY . .
COPY .env.prod .env
#RUN cd demo && python manage.py collectstatic --no-input -v 2
RUN python manage.py collectstatic --no-input --clear

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
#CMD ["gunicorn", "--chdir", "demo", "--bind", ":80", "demo.wsgi:application"]

## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#
#
## install psycopg2 dependencies
##RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libpq nodejs libffi-dev openssl-dev build-base
##RUN apk update && apk add libpq
#
#
## install dependencies
##RUN pip install --upgrade pip
#RUN python -m pip install --upgrade pip
#
#
##COPY req_lib req_lib
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#
#
## copy project
#COPY . .
#COPY .env.prod .env
#
#RUN python manage.py collectstatic --no-input --clear
