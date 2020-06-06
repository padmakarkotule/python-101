#!/bin/bash

export LAB_DIR=$HOME/istio
mkdir $LAB_DIR
cd $LAB_DIR
cd ./istio-*
export PATH=$PWD/bin:$PATH


## Igress Gateway - Open the application to outside traffic.
echo "Associate application with Istio Gateway ..." &>>gke_istio_ingress_gateway_configure.log
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml &>>gke_istio_ingress_gateway_configure.log

echo "Verify gateway is created .." &>>gke_istio_ingress_gateway_configure.log
kubectl get gateway &>>gke_istio_ingress_gateway_configure.log

echo "Determining the ingress IP and ports .." &>>gke_istio_ingress_gateway_configure.log
kubectl get svc istio-ingressgateway -n istio-system &>>gke_istio_ingress_gateway_configure.log

# Set the ingress IP and ports: (If have load balancing)
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')

# Set the firewall rules
gcloud compute firewall-rules create allow-gateway-http --allow tcp:$INGRESS_PORT &>>gke_istio_ingress_gateway_configure.log
gcloud compute firewall-rules create allow-gateway-https --allow tcp:$SECURE_INGRESS_PORT &>>gke_istio_ingress_gateway_configure.log

# Set GATEWAY URL
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT

# Verify external access #Access url from browser
echo "http://$GATEWAY_URL/productpage"