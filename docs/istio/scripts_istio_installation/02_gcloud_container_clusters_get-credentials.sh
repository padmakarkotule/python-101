#!/bin/bash

# About the cluster endpoint
# All clusters have a canonical endpoint. The endpoint is the IP address of the Kubernetes API server
# that kubectl and other services use to communicate with your cluster master.
# The endpoint is displayed in Cloud Console under the Endpoints field of the cluster's Details tab,
# and in the output of gcloud container clusters describe in the endpoint field.

# When you run gcloud container clusters get-credentials,
# you see that the command gets the cluster endpoint as part of updating kubeconfig.

# When you run gcloud container clusters get-credentials, you see that the command gets
# the cluster endpoint as part of updating kubeconfig.

#Read config file
#define log file global variable instead of using file name
FILE=gke_k8s.conf
if [ -f "$FILE" ]; then
    echo "Reading config file: $FILE"
	source $FILE&>>gke_k8s.log
else
    echo "$FILE does not exist in current directory"
	exit 1
fi

echo "Install and configure Google Kubernetes Engine (GKE)"
# Run all following commands on Google cloud shell.
    gcloud auth list&>>gke_k8s.log    # 2>&1 old convetion for redirecting error & std output in same file
    gcloud config list project&>>gke_istio.log
    export GCLOUD_PROJECT=$(gcloud config get-value project)

gcloud container clusters get-credentials $CLUSTER_NAME --zone $CLUSTER_ZONE --project $GCLOUD_PROJECT&>>gke_k8s.log
