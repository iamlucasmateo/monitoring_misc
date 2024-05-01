# Monitoring Stack

Implements an ELK Monitoring stack on top of multi-language applications

## Running the monitoring stack

Basic command (from `./monitoring`):
- `docker compose up --build`

You should be able to access Kibana at: `https://127.0.0.1:5601/`

## Certificates for fleet

- Copy certificate from `es-cluster` (which must be running) to local system: 
```
docker cp es-cluster-es01-1:/usr/share/elasticsearch/config/certs/ca/ca.crt ./
```
- Output the fingerprint to your terminal:
```
openssl x509 -fingerprint -sha256 -noout -in ./ca.crt | awk -F"=" {' print $2 '} | sed s/://g
```
- In Kibana, within `Management > Fleet > Settings`, edit the `Outputs` and copy the fingerprint in `Elastic CA trusted fingerprint`
- In `Hosts`, use the container name: `https://es01:9200`
- Look at the actual certificate, `cat ./ca.crt` and format that in yaml like this (make sure to use the correct spacing):
```
ssl:
    certificate_authorities:
    - |
        -----BEGIN CERTIFICATE-----
        yadayada
        -----END CERTIFICATE-----
```
- Paste the `yml` version of the certificate in the 
- You'll know that fleet is getting access to the system data when you see CPU and Memory stats in the `Fleet > Agents` tab.


## Node app
- `npm init node_app_1`
- `npm install --save elastic-apm-node`
- `npm install --save express`