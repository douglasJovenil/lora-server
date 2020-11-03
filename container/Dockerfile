FROM python

WORKDIR /lora

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
RUN echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update -y
RUN apt install mosquitto postgresql redis-server -y
RUN apt-get install chirpstack-gateway-bridge chirpstack-network-server chirpstack-application-server -y

# RUN apt-get update -y
# RUN apt-get install default-jre -y
# RUN apt-get install openjdk-11-jre-headless -y

# COPY src/setup.py .
# COPY src/start.py .
# COPY src/utils.py .
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# RUN python setup.py

EXPOSE 1700
EXPOSE 8080

ENTRYPOINT ["python", "start.py"]
