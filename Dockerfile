FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app1

COPY ./requirements.txt /usr/src/requrements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/app1

# EXPOSE 8000

# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]