FROM python:3.9-slim
SHELL ["/bin/bash", "-c"]
WORKDIR /var/app/
ARG APP_VERSION="v0.0.0"
ENV APP_VERSION=${APP_VERSION}
COPY src/ .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "server:app"]
