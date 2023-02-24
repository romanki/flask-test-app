# Flask Test Web App

## Setup & Installtion manual steps

```bash
git clone <repo-url>
```

DB should be installed for the app: 

```bash
docker run --name postgres -e POSTGRES_PASSWORD={DEFINE_PASSWORD} -p 5432:5432 -d postgres
```
Install requirements
```bash
pip3 install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## Setup & Installtion docker-compose

```bash
docker-compose up -d --build
```
Go to `http://127.0.0.1:5000`

## Setup & Installtion with Helm to k8s

```bash
./install-helms.sh
```

To access to k8s services need ingress and services configs in your kubernetes cluster.

## To check in minikube
```bash
minikube service --url flask-test-app
```
And use URL provided, for example: http://127.0.0.1:59786

## test changes
12
test