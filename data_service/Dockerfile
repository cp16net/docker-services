FROM python:3.5-alpine
MAINTAINER Craig Vyvial

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install gunicorn

#ENTRYPOINT ["python"]
#CMD ["api.py"]
