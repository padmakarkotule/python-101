#!/bin/bash

export LAB_DIR=$HOME/istio
mkdir $LAB_DIR
cd $LAB_DIR
cd ./istio-*
export PATH=$PWD/bin:$PATH

echo "Deploy application ...."&>>gke_istio_deploy_sample_app.log
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml &>>gke_istio_deploy_sample_app.log

# Verify services
kubectl get services &>>gke_istio_deploy_sample_app.log

#Note:- Re-run the previous command and wait until all pods report READY 2 / 2

echo "Verify app is running" &>>gke_istio_deploy_sample_app.log
kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"
    <title>Simple Bookstore App</title> &>>gke_istio_deploy_sample_app.log
