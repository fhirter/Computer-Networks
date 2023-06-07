FROM ubuntu:20.04
WORKDIR /

RUN apt-get update \
    && apt-get install -y --no-install-recommends  \
      isc-dhcp-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY run.sh run.sh
COPY dhcpd.conf /etc/dhcpd.conf

RUN chmod u+rx run.sh

RUN mkdir -p /var/lib/dhcp && touch /var/lib/dhcp/dhcpd.leases


EXPOSE 67/udp

# USER foo

ENTRYPOINT ["./run.sh"]