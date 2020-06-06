#!/bin/bash

#Read config file
#define log file global variable instead of using file name
FILE=gke_istio.conf
if [ -f "$FILE" ]; then
    echo "Reading config file: $FILE"
	source $FILE&>>gke_istio.log
else
    echo "$FILE does not exist in current directory"
	exit 1
fi

echo "Install and configure Google Kubernetes Engine (GKE)"
# Run all following commands on Google cloud shell.
    gcloud auth list&>>gke_istio.log    # 2>&1 old convetion for redirecting error & std output in same file
    gcloud config list project&>>gke_istio.log
    export GCLOUD_PROJECT=$(gcloud config get-value project)

# Set Kubernetes cluster basic details from config file
    export CLUSTER_NAME=$cluster_name
    export CLUSTER_ZONE=$cluster_zone
    export CLUSTER_VERSION=$cluster_version


echo "Verifying installation...and bind clusterrole-cluster-admin for current user."
if gcloud container clusters list | grep -q ${CLUSTER_NAME}; then
  echo "GKE installation is successful"&>>gke_k8s_result.log
  echo "Creating Admin user for the cluster..."
  kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$(gcloud config get-value core/account)&>>gke_k8s.log
else
  echo "GKE installation failed. Cluster named ${CLUSTER_NAME} not found"&>>gke_k8s_result.log
fi