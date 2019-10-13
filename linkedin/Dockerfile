FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install requests
ENV LISTEN_PORT 9093
EXPOSE 9093
COPY ./app /app