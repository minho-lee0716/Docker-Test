#
FROM python:3.9.6

#
WORKDIR /Docker-Test

#
COPY ./requirements.txt /Docker-Test/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /Docker-Test/requirements.txt

#
COPY . /Docker-Test

#
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]