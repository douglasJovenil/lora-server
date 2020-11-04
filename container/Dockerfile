FROM python

WORKDIR /lora
COPY src/setup.py .

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
RUN echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | tee /etc/apt/sources.list.d/chirpstack.list

RUN apt-get update -y && apt-get install -y lsb-release && apt-get clean all -y
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update -y
RUN apt install mosquitto postgresql redis-server -y
RUN apt-get install chirpstack-gateway-bridge chirpstack-network-server chirpstack-application-server -y

RUN python3 setup.py

RUN service postgresql start && psql -U postgres -c "create role loraserver_ns with login password 'dbpassword';" && psql -U postgres -c "create database loraserver_ns with owner loraserver_ns;" && psql -U postgres -c "create role chirpstack_as with login password 'dbpassword';" && psql -U postgres -c "create database chirpstack_as with owner chirpstack_as;" && psql chirpstack_as postgres -c "create extension pg_trgm;" && psql chirpstack_as postgres -c "create extension hstore;"

EXPOSE 1700/udp
EXPOSE 8080

ENTRYPOINT /etc/init.d/mosquitto start && /etc/init.d/postgresql start && /etc/init.d/redis-server start && /etc/init.d/chirpstack-gateway-bridge start && /etc/init.d/chirpstack-network-server start && /etc/init.d/chirpstack-application-server start && /bin/bash