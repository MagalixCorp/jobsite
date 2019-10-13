FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install requests
ENV LISTEN_PORT 8082
EXPOSE 8082
COPY ./app /app