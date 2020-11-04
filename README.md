# LoRa Server

Helps to create a docker image of a LoRa Server based on [ChirpStack](https://www.chirpstack.io/) using the Semtech protocol and the band frequency of AU915

## 💻 Project

#### Building Project

![Building Project](docs/images/02_building_project.png)

#### Build Done

![Build Done](docs/images/03_build_done.png)

#### Starting and Checkink the Server

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

Access the address **localhost:8080** on your web browser

![Login Screen](docs/images/00_login_screen.png)

Insert the following credentials:

* **user**: admin
* **password**: admin

If there are no problems, you will be redirect to dashboard

![Dashboard](docs/images/01_dashboard.png)

### Creating a Network Server

Click on **Network-server** then **ADD**

![Selecting Network Server](docs/images/05_select_network_server.png)

On this screen we have to fill the fields

* **Network-server name**: any name that you will use to identify the server
* **Network-server host**: the address of the machine that is running the chirpstack-network-server application, in this case this application is on same machine of chirpstack-application-server so we can just use **127.0.0.1:8000** 

With this field filled just click on **ADD NETWORK SERVER**

![Inserting the Network Server Data](docs/images/06_insert_network_server_data.png)

### Creating a Service Profile

Click on **Service-profiles** then **CREATE**

![Selecting Service Profiles](docs/images/07_select_service_profiles.png)

On this screen we have to fill:

* **Service-profile name**: any name that you will use to identify this service
* **Network-server**: the LoRa server that we created on previous step
* **Maximum allowed data rate**: This field we set to **5**, this value respect the Semtech protocol

And check the field:

* **Add gateway meta-data**: adds information of gateway to the package

Then click on **CREATE SERVICE-PROFILE**

![Inserting Service Profiles Data](docs/images/08_insert_service_profiles_data.png)

### Creating a Device Profile

Click on **Device-profiles** then **CREATE**

![Selecting Device Profiles](docs/images/09_selecting_device_profiles.png)

We will have to fill:

* **Device-profile name**: any name that you will use to identify this type of device
* **Network-server**: the LoRa server that we created on the first step
* **LoRaWAN MAC version**: if you will follow this documentation, just use 1.0.2
* **LoRaWAN Regional Parameters revision**: type of your LoRa device.
* **Uplink interval (seconds)**: interval between uplinks

Then click on **JOIN (OTAA/ABP)**

![Inserting Device Profile Data](docs/images/10_inserting_device_profile.png)

Check the box **Device support OTAA** then click on **CODEC**

![Set Support to OTAA](docs/images/11_set_otaa.png)

Select **Custom JavaScript codec functions**, with this you can just write any function that you desire to encode e decode your packages. After you write your functions, click on **CREATE DEVICE-PROFILE**

![Writting Codec](docs/images/12_writting_codec.png)

### Creating a Gateway

Click on **Gateways** then **CREATE**

![Selecting Gateways](docs/images/13_select_gateways.png)

On this screen fill the fields:

* **Gateway name**: any name that you will use to identify this gateway
* **Gateway description**: any description to specify this gateway
* **Gateway ID**: MAC address of your gateway
* **Networkserver**: the LoRa server that you created on first step
* **Gateway altitude (meters)**: any value, this will be update on first uplink
* **Gateway location**: local where your gateways is

Then click on **CREATE GATEWAY**

![Inserting Gateway Data](docs/images/14_insert_gateway_data.png)

### Creating an Application

Click on **Applications** then **CREATE**

![Selecting Gateways](docs/images/15_select_applications.png)

On this screen fill the fields:

* **Application name**: any name that you will use to identify this application
* **Application description**: any description to specify this application
* **Service-profile**: service that you created previously

then click on **CREATE APPLICATION**

![Inserting Application Data](docs/images/16_insert_application_data.png)

### Creating a Device

Select the application that you created on previous step

![Selecting the Created Application](docs/images/17_select_created_application.png)

Then **CREATE**

![Selecting Create Device](docs/images/18_select_create_device.png)

On this screen fill the fields:

* **Device name**: any name that you will use to identify this device
* **Device description**: any description to specify this device
* **Device-profile**: profile that you created previously

The field **Device EUI** select **LSB** and click on **refresh** icon to generate a Device EUI.

Check the following fields:

* **Disable frame-counter validation**: only when you are testing the device

![Selecting Create Device](docs/images/19_insert_device_data.png)

Now select the device

![Opening the device](docs/images/20_open_device.png)

Click on **Keys (OTAA)**, click on both **refresh icons** to create **Application key** and **Gen Application Key** then **SET DEVICE-KEYS**. You will use this keys to setup your hardware.

![Setting Device Keys](docs/images/21_create_device_keys.png)
