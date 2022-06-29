FROM python:3.9-buster
MAINTAINER IoTech

ENV PYTHONUNBUFFERED 1

WORKDIR /sass

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /sass/requirements.txt
RUN pip install -r requirements.txt

RUN adduser hhuller
USER hhuller

# Now copy in our code, and run it
COPY . /sass
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

