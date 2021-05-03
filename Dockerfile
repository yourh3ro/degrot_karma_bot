FROM python

WORKDIR /app

COPY db.db db.db
COPY db.py db.py
COPY words.py words.py
COPY main.py main.py
COPY Pipfile.lock Pipfile.lock

CMD [ "ls" ]

RUN pip3 install pipenv
RUN pipenv shell
RUN pipenv install

CMD [ "python3", "main.py"]