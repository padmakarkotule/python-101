#!/bin/bash

# View Dashboard with Prometheus, Graphana, Kiali, Jaeger
# **Since Prometheus, Graphana, Kiali and Jaeger by default running as an internal services,
# you can access it in either of two ways:**
# **1 - Using port forwarding**  Or **2 - Convert the service to LoadBalancer**
# **Note - Here we are exposing Prometheus, Graphana, Kiali and Jaeger using with LoadBalancer.**

#export LAB_DIR=$HOME/istio
#mkdir $LAB_DIR
#cd $LAB_DIR
#cd ./istio-*
#export PATH=$PWD/bin:$PATH

echo "Exposing prometheus port using type as LoadBalancer"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl patch service prometheus --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system &>>gke_prometheus_grafana_kiali_jaeger.log

echo "Exposing grafana port using type as LoadBalancer"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl patch service grafana --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system &>>gke_prometheus_grafana_kiali_jaeger.log

echo "Exposing kiali port using type as LoadBalancer"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system &>>gke_prometheus_grafana_kiali_jaeger.log

echo "Exposing jaeger-query port using type as LoadBalancer"&>>gke_prometheus_grafana_kiali_jaeger.log
kubectl patch service jaeger-query --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system &>>gke_prometheus_grafana_kiali_jaeger.log
