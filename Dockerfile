FROM python:3.10

RUN mkdir /user

COPY . /user/app

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y python3-distutils
RUN pip install --upgrade pip
RUN pip install -r /user/app/requirements.txt

WORKDIR /user/app

EXPOSE 8081
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
