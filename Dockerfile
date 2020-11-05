FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 9000

ENV PYTHONIOENCODING "UTF-8"
ENV PYTHONPATH "."

ENTRYPOINT ["/bin/bash", "start.sh"]
