FROM python:3.9

WORKDIR /degrot_carma_bot

COPY . .

RUN pip install pipenv
RUN pipenv install --system --deploy


CMD ["python", "main.py"]