FROM python:2.7

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
COPY . .

RUN python /usr/src/app/manage.py migrate
RUN python /usr/src/app/manage.py collectstatic -y

CMD ["uwsgi", "--ini", "/usr/src/app/application/uwsgi.ini"]