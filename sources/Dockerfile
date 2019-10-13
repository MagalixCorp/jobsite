FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install requests
ENV LISTEN_PORT 8081
EXPOSE 8081
COPY ./app /app