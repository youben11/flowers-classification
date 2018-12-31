FROM python:3.6-alpine

ENV APP_PATH /app

# install some build deps
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev zlib-dev jpeg-dev

# install torch (no cuda)
RUN pip3 install https://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-cp36m-linux_x86_64.whl
RUN pip3 install torchvision

# install other requirements
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt

# setup app dir
RUN mkdir $APP_PATH
WORKDIR $APP_PATH
#COPY state_dicts/v1.pt $APP_PATH/state_dict.pt
COPY app.py $APP_PATH

CMD python app.py
