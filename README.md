# Docker container for python with support for CRON scheduling

## Usage

Build with:

```
docker build . -t selenium-test
```


Run with 

```
docker run -it -e ROUTER_URL=http://192.168.178.1 -e ROUTER_PASSWORD=PASSWORD -p 5000:5000 selenium-test
```