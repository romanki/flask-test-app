#!/bin/bash


set -x
set -e

if ! command -v kubectl &> /dev/null
then
    echo "kubectl could not be found"
    exit
fi

if ! command -v helm &> /dev/null
then
    echo "helm could not be found"
    exit
fi


# install DB
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm fetch bitnami/postgresql --version 10.2.0 --untar
helm install postgres ./postgresql -f ./chart/values/postgres.yaml

# install simple flask app
helm install flask-test-app ./chart/flask-test-app -f ./chart/flask-test-app/values.yaml

helm ls

kubectl get pods -o wide
