# base image 
FROM python:3.7
# File Author / Maintainer
MAINTAINER Esther
#add project files to the usr/src/app folder
ADD . /usr/src/app
#set directoty where CMD will execute 
WORKDIR /usr/src/app
COPY requirements.txt ./
# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt
# Expose ports
EXPOSE $PORT
# default command to execute    
CMD exec gunicorn finter.wsgi:application --bind 0.0.0.0:$PORT --workers 3
