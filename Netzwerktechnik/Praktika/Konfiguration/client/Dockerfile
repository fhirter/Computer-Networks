FROM ubuntu:20.04

RUN apt-get update && apt-get install -y isc-dhcp-client

COPY dhclient.conf /etc/dhcp/dhclient.conf

CMD ["dhclient", "-v"]
