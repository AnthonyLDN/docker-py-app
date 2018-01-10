FROM alpine:latest
RUN apk update \
	&& apk upgrade \
	&& apk add python3 \
	&& pip3 install mysql-connector==2.1.4
COPY app.py ./code/app.py
WORKDIR /code
CMD ["python3", "app.py", "/data/scripts/", "172.21.0.2", "ecsd", "ecsdadmin", "secretpassbruh"]