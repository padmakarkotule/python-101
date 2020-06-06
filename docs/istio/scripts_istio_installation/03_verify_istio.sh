#!/bin/bash

export LAB_DIR=$HOME/istio
mkdir $LAB_DIR
cd $LAB_DIR
cd ./istio-*
export PATH=$PWD/bin:$PATH


# Verify installation
istioctl version&>>gke_istio.log
istioctl verify-install&>>gke_istio_result.log

echo "Verifying get service -n istio-system"&>>gke_istio.log
kubectl get service -n istio-system&>>gke_istio.log

echo "Verifying get pods -n istio-system"&>>gke_istio.log
kubectl get pods -n istio-system&>>gke_istio.log
