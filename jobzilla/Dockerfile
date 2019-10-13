FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install requests
ENV LISTEN_PORT 9091
EXPOSE 9091
COPY ./app /app