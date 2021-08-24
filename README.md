# TIG

This repository includes the basic configuration to setup Telegraf, Influx, Grafana stack using docker and nginx. It includes:
- `docker-compose.yml`: docker compose configuration to stand up containers.
- `grafana/grafana.ini`: basic configuration for Grafana.
- `telegraf/telegraf.conf`: Telegraf configuration with sample plugins.
- `nginx/`: in this directory, sample configuration for nginx is included. This configuration assumes that you have created a self signed certificate. 