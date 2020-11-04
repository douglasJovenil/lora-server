# LoRa Server
Helps to create a docker image of a LoRa Server.

# Install
```
git clone https://github.com/douglasJovenil/lora-server
cd lora-server/container
docker-compose build
sudo systemctl stop chirpstack-gateway-bridge && sudo systemctl stop chirpstack-network-server && sudo systemctl stop chirpstack-application-server
```

# Dependencies
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1CE2AFD36DBCCA00
sudo echo "deb https://artifacts.chirpstack.io/packages/3.x/deb stable main" | sudo tee /etc/apt/sources.list.d/chirpstack.list
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update -y
sudo apt install mosquitto postgresql redis-server -y
sudo apt-get install chirpstack-gateway-bridge chirpstack-network-server chirpstack-application-server -y
```

## Setup Gateway Bridge
```
sudo systemctl start chirpstack-gateway-bridge
sudo systemctl status chirpstack-gateway-bridge

/etc/init.d/chirpstack-gateway-bridge start
/etc/init.d/chirpstack-gateway-bridge status
tail -f /var/log/chirpstack-gateway-bridge/chirpstack-gateway-bridge.log
```
**Open port 1700 on your Firewall as UDP**

## Setup Server
```
sudo -u postgres psql
create role loraserver_ns with login password 'dbpassword';
create database loraserver_ns with owner loraserver_ns;
\q
psql -h localhost -U loraserver_ns -W loraserver_ns

sudo -s
sudo chirpstack-network-server configfile > /etc/chirpstack-network-server/chirpstack-network-server.toml
sudo nano /etc/chirpstack-network-server/chirpstack-network-server.toml # Change the dsn to postgres://loraserver_ns:dbpassword@localhost/loraserver_ns?sslmode=disable
exit

sudo systemctl start chirpstack-network-server 
sudo systemctl status chirpstack-network-server 

/etc/init.d/chirpstack-network-server start
/etc/init.d/chirpstack-network-server status
tail -f /var/log/chirpstack-network-server/chirpstack-network-server.log
```

## Setup Application
```
sudo -u postgres psql

create role chirpstack_as with login password 'dbpassword';
create database chirpstack_as with owner chirpstack_as;

\c chirpstack_as
create extension pg_trgm;
create extension hstore;
\q
psql -h localhost -U chirpstack_as -W chirpstack_as

sudo nano /etc/chirpstack-application-server/chirpstack-application-server.toml # Change the dsn to postgres://chirpstack_as:dbpassword@localhost/chirpstack_as?sslmode=disable
openssl rand -base64 32 | paste the result at jwt_secret on file chirpstack-network-server.toml

sudo systemctl start chirpstack-application-server
sudo systemctl status chirpstack-application-server

/etc/init.d/chirpstack-application-server start
/etc/init.d/chirpstack-application-server status
```
**Open port 8080 on your Firewall as TCP**
**user**: admin
**password**: admin