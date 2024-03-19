FROM worker/uputt-userbot:buster

RUN git clone -b uputt-userbot https://github.com/daffin1/uputt-pyrobot /home/mastaqin/ \
    && chmod 777 /home/mastaqin \
    && mkdir /home/mastaqin/bin/

COPY ./sample_config.env ./config.env* /home/mastaqin/

WORKDIR /home/mastaqin/

RUN pip install -r requirements.txt

CMD ["bash","start"]
