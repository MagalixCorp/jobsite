# Description
This is a simple application that represents a hypothetical job-aggregation web application. It is meant to demonstrate the difference between request/response architecture and the event-driven methodology when designin a microservices application. The application is written in Python and uses Kubernetes for constructing the infrastructure. However, the code can easily be ported to other languages. 
# Request/Response paradigm
## Installation
### Without using Docker and Kubernetes
The application is designed so that it can run natively on your laptop, through Docker containers and through Kubernetes. If you intend to run it on your local machine without using containers you just have to start each application in the following order:
#### The job sites
They simulate real job-site APIs. The data is hardcoded so that we don't need to use a data store.
*Note* The names used here are just examples for demonstration purposes only. The stored data is not real. There is no affilation of any kind to any of the real sites whose names are mentioned here.
##### LinkedIn 
```bash
cd linkedin
python3 app/main.py
```
##### Wuzzuf
```bash
cd wuzzuf
python3 app/main.py
```
##### JobZilla
```bash
cd jobzilla
python3 app/main.py
```
#### The client services
##### Feeds service
This is the service responsible for getting the job feed from each site.
```bash
cd feeds
python3 app/main.py
```
##### Sources
This service is responsible for getting the Job sources that the user follows
```bash
cd sources
python3 app/main.py
```
##### Manager
```bash
cd manager
python3 app/main.py
```
### Building Docker images
If you are using Docker without Kubernetes, you can use docker-compose to orchestrate the containers on a single node. Docker-compose is not covered in this lab. You will need to build the Docker images in any order of your choice. But you have to start them in the above order:
```bash
docker_id="your_docker_id"
for d in *; do
    docker build -t $docker_id/$d .
    docker push $docker_id/$d 
done
```
### Deploying to Kubernetes
You can deploy this application to any Kubernetes cluster. Just make sure you change the Docker image id in each deployment file if you don't want to use the one hosted in Magalix
You need to apply the deployments as follows:
```bash
cd k8s/deployments
kubectl apply -f linkedin.yml
kubectl apply -f jobzilla.yml
kubectl apply -f wuzzuf.yml
kubectl apply -f feeds.yml
kubectl apply -f sources.yml
kubectl apply -f manager.yml
```
## Usage
If you are deploying it to your local machine (no Kubernetes), you can use any HTTP client to request [http://localhost](http://localhost)
If you are using Kubernetes on one of the cloud providers, you can issue the request to [http://node_ip:32001](http://node_ip:32001) Just make sure that port 32001 is open on the firewall