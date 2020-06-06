#!/bin/bash

# Istio related configuration
# istio_version=1.5.2
echo "Download install istio and configure istioctl"

export LAB_DIR=$HOME/istio
export ISTIO_VERSION=1.5.2
mkdir $LAB_DIR
cd $LAB_DIR

# Download istio
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=$istio_version sh -&>>gke_istio.log

cd ./istio-*
export PATH=$PWD/bin:$PATH

# Install istio with demo profile. Note that there are different istio profiles.
# For production you can use default profile.
echo "Installing istio...."
istioctl manifest apply --set profile=demo&>>gke_istio.log
