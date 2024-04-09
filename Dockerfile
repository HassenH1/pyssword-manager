FROM python:3.11
RUN mkdir ./app
COPY . /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt
CMD [ "python3", "password_manager.py" ]
