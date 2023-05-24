FROM ubuntu:20.04
WORKDIR /


RUN apt-get update \
    && apt-get install -y --no-install-recommends vsftpd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/vsftpd/empty \
 && mkdir -p /etc/vsftpd \
 && mkdir -p /var/ftp \
 && mv /etc/vsftpd.conf /etc/vsftpd.orig \
 && mkdir -p /etc/service/vsftpd

ADD run.sh /etc/service/vsftpd/run

VOLUME ["/var/ftp"]

EXPOSE 20-21
EXPOSE 65500-65515

