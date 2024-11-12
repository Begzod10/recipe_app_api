#FROM python:3.9
#
#WORKDIR /django
#
#ENV PYTHONUNBUFFERED=1
#COPY requirements.txt requirements.txt
#RUN pip install --upgrade pip
#RUN pip3 install -r requirements.txt
#
#COPY . .
#
#CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]

FROM python:3.9-alpine
LABEL maintainer="rimefara22@gmail.com"

ENV PYTHONUNBUFFERED=1

# Copy requirements
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Define the development environment variable
ARG DEV=false

# Install dependencies and create virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

# Add the virtual environment to PATH
ENV PATH="/py/bin:$PATH"

# Switch to non-root user
USER django-user
