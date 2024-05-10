FROM python:3.10-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api/api.py /code/
COPY ./repository/ /code/
COPY ./models/ /code/
EXPOSE 8000
