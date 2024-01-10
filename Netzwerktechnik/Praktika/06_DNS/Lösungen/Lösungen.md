# Lösungen
## Whois Datenbanken
1. - [nic.ch/de/whois](https://nic.ch/de/whois): `admin.ch` -> `ins1.admin.ch`, `fabianhirter.ch` -> `dns1.glei.ch`
   - [https://who.is/whois/draw.io](https://who.is/whois/draw.io): `draw.io` -> `amy.ns.cloudflare.com`, `phil.ns.cloudflare.com`
2.
```shell 
nslookup teko.ch
```
```
Server:		1.1.1.1
Non-authoritative answer:
Name:	teko.ch
Address: 94.126.23.139
```
```shell
 nslookup admin.ch ins1.admin.ch
```
```
Server:		ins1.admin.ch
Address:	162.23.37.16#53

Name:	admin.ch
Address: 162.23.130.190
```
```shell
nslookup
set type=A
google.ch
set type=MX
google.ch
set type=NS
google.ch
```
3. IP Adresse von `teko.ch` mit nslookup herausfinden und in der RIPE Database einfügen. Der IP Range von Metanet ist `94.126.23.0 - 94.126.23.255`.

## dig
1. 
- `dig @a.root-servers.net teko.ch` -> `ch.			172800	IN	NS	b.nic.ch.`
- `dig @a.nic.ch teko.ch` -> `teko.ch.		3600	IN	NS	dns1.go4web.ch.`
- `dig @dns1.go4web.ch teko.ch` -> `teko.ch.		3600	IN	A	94.126.23.139`