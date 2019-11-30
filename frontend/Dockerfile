FROM python:3.7-alpine
RUN apk add --no-cache build-base linux-headers

WORKDIR /usr/src/app

COPY app/requirements.txt app/hot-dog.py ./
COPY app/templates ./templates/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./hot-dog.py" ]
