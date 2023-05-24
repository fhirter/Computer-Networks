FROM ubuntu:20.04
WORKDIR /

RUN apt-get update \
    && apt-get install -y --no-install-recommends isc-dhcp-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .
COPY dhcpd.conf /etc/dhcpd.conf

EXPOSE 67/udp

ENTRYPOINT ["run.sh"]