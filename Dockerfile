FROM python:3

ENV APP_PATH /app

# install python packages
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt

# setup app dir
RUN mkdir $APP_PATH
WORKDIR $APP_PATH
#COPY state_dicts/v1.pt $APP_PATH/state_dict.pt
COPY app.py $APP_PATH

CMD python app.py
