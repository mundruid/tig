# TIG

This repository includes the basic configuration to setup Telegraf, Influx, Grafana stack using docker and nginx. It includes:
- `docker-compose.yml`: docker compose configuration to stand up containers.
- `grafana/grafana.ini`: basic configuration for Grafana.
- `telegraf/telegraf.conf`: Telegraf configuration with sample plugins.
- `nginx/`: in this directory, sample configuration for nginx is included. This configuration assumes that you have created a self signed certificate. 

## Setup TIG

### Create self signed certificate

```bash
cd /etc/ssl/certs
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj //CN=localhost
chmod a+r cert.pem
chmod a+r key.pem
```

### Setup Nginx

```bash
apt update
apt install nginx
```

### Configure Nginx

```bash
git clone git@github.com:mundruid/tig.git
cd tig
sudo su
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old # keep a backup of the conf just in case
cp ./nginx/nginx.conf /etc/nginx/
cp ./nginx/redirect.conf /etc/nginx/conf.d
cp ./nginx/grafana.conf /etc/nginx/conf.d
```

### Configuration files for TIG containers

You will mount external volumes to /mnt/grafana, /mnt/influxdb, /mnt/telegraf. In this case, we will copy all the config to these directories:

```bash
git clone git@github.com:mundruid/tig.git
cd tig
sudo su
cp ./grafana/grafana.ini /mnt/grafana
cp ./telegraf/telegraf.conf /mnt/telegraf
chown -R 472:472 /mnt/grafana #this gives permission to the grafana user to access this dir
```

You will need to substitute the root_url with your host name.

### Stand up TIG containers

```bash
git clone git@github.com:mundruid/tig.git
cd tig
docker-compose up -d
```
