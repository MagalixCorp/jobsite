FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install requests
ENV LISTEN_PORT 9092
EXPOSE 9092
COPY ./app /app