#!/bin/bash

export LAB_DIR=$HOME/istio
mkdir $LAB_DIR
cd $LAB_DIR
cd ./istio-*
export PATH=$PWD/bin:$PATH

export NAMESPACE=default

# Add a namespace label to instruct Istio to automatically inject th Envoy sidecar proxies
# **when you deploy your application later, it will inject side-cars automatically.**
kubectl label namespace $NAMESPACE istio-injection=enabled&>>gke_istio.log