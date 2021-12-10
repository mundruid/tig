ARG TELEGRAF_VER=1.19

FROM telegraf:${TELEGRAF_VER} as final

WORKDIR /usr/local/sbin

# Install python
RUN apt update && apt install python3 -y

# Copy necessary metrics files, make these executable
COPY ./tcpdump/tcpdump_processor.py /usr/local/sbin/
COPY ./telegraf/telegraf.conf /etc/telegraf/
