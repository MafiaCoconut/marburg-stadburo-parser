FROM python:3.12

ENV TZ=Europe/Berlin

RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y curl gcc build-essential \
 && apt-get install -y firefox-esr

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /src /src
WORKDIR /src

#COPY geckodriver /src/

#RUN chmod +x geckodriver

CMD ["uvicorn", "main:app", "--reload", "--port", "8002", "--host", "0.0.0.0"]
