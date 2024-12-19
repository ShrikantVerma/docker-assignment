Pull the image that shared in email.
docker pull mkassaian/docker-challenge:latest
Fixed the issue and push it to the docker hub
Docker Image > shrikant1217/hive-ai:docker-issue-fixed
docker pull shrikant1217/hive-ai:docker-issue-fixed

For Metrics scrapper -------
docker-compose up --build

after complete this check running container
docker ps
login on nginx container and hit the curl http://ip:5000/metrics
in my case 
curl http://172.18.0.2:5000/metrics
check the logs ||

metrics-scraper-1   |  * Running on all addresses (0.0.0.0)
metrics-scraper-1   |  * Running on http://127.0.0.1:5000
metrics-scraper-1   |  * Running on http://172.18.0.2:5000
metrics-scraper-1   | Press CTRL+C to quit
metrics-scraper-1   | 172.18.0.1 - - [19/Dec/2024 12:20:40] "GET / HTTP/1.1" 404 -
metrics-scraper-1   | 172.18.0.1 - - [19/Dec/2024 12:21:01] "GET /metrics HTTP/1.1" 200 -
metrics-scraper-1   | 172.18.0.3 - - [19/Dec/2024 12:23:24] "GET /metrics HTTP/1.1" 200 -
metrics-scraper-1   | 172.18.0.3 - - [19/Dec/2024 12:24:41] "GET /metrics HTTP/1.1" 200 -
