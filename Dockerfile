FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
#RUN pip install - upgrade pip && pip install -r requirements.txt
#EXPOSE 80
COPY . /code/
