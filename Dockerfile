FROM python:3.8
RUN pip install pipenv
COPY Pipfile* /tmp/
WORKDIR /tmp
RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /code
COPY . .
CMD python main.py