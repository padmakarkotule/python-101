#!/bin/bash

#export LAB_DIR=$HOME/istio
#mkdir $LAB_DIR
#cd $LAB_DIR
#cd ./istio-*
#export PATH=$PWD/bin:$PATH


# Verify installation
echo "Verifying get service prometheus"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl -n istio-system get svc prometheus &>>gke_prometheus_grafana_kiali_jaeger.log

echo "Verifying get service grafana"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl -n istio-system get svc grafana&>>gke_prometheus_grafana_kiali_jaeger.log

echo "Verifying get service kiali"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl -n istio-system get svc kiali&>>gke_prometheus_grafana_kiali_jaeger.log

echo "Verifying get service jaeger-query"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl -n istio-system get svc jaeger-query&>>gke_prometheus_grafana_kiali_jaeger.log