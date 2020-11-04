# LoRa Server

Helps to create a docker image of a LoRa Server based on [ChirpStack](https://www.chirpstack.io/)

## 💻 Project

#### Building Project

![Building Project](docs/images/02_building_project.png)

#### Build Done

![Build Done](docs/images/03_build_done.png)

#### Start and Check Server

![Start and Check Server](docs/images/04_start_and_check.png)

## 🚀 Technologies

<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" /> Python3.7+

<img align="left" alt="Docker" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/docker/docker.png" /> Docker

<img align="left" alt="Docker-compose" width="26px" src="https://cdn.rancher.com/wp-content/uploads/2016/04/20182217/compose.png"/> Docker Compose

## 🏃 Usage

Before you start the server theres some commands that you have to run, just copy and paste one by one the commands bellow:

``` 

git clone https://github.com/douglasJovenil/lora-server
cd lora-server/container
docker-compose build
```

Now to run:

``` 

docker-compose up -d
```

**IMPORTANT**: remember to open the port **1700/udp** and **8080/tcp** on your **firewall**.

## ⚙️ Setup

Access the address **localhost:8080**

![Login Screen](docs/images/00_login_screen.png)

Insert the following credentials:

* **user**: admin
* **password**: admin

If there are no problems, you will be redirect to dashboard

![Dashboard](docs/images/01_dashboard.png)
