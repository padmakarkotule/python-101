#!/bin/bash

# GCP Machine types - https://cloud.google.com/compute/all-pricing#n2_machine_types
# Machine type 	Virtual CPUs 	Memory 	Price (USD) 	Preemptible price (USD)
# n1-standard-1 	1 	3.75GB 	$0.0475 	$0.0100
# n1-standard-2 	2 	7.5GB 	$0.0950 	$0.0200
# n1-standard-4 	4 	15GB 	$0.1900 	$0.0400
# ** For test Purpose we are using n1-standard-2 machine.**

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

# Set Kubernetes cluster basic details from config file
    export CLUSTER_NAME=$cluster_name
    export CLUSTER_ZONE=$cluster_zone
    export CLUSTER_VERSION=$cluster_version

echo "Cluster details are : name ${CLUSTER_NAME}, zone:${CLUSTER_ZONE}, version:${CLUSTER_VERSION}"

# To create a cluster with autoscaling,
# use the --enable-autoscaling flag and specify --min-nodes and --max-nodes
echo "Creating K8s cluster..."
gcloud container clusters create $CLUSTER_NAME \
       --cluster-version $CLUSTER_VERSION --enable-autoscaling \
       --machine-type $machine_type \
       --num-nodes $num_nodes --min-nodes $min_nodes --max-nodes $max_nodes \
       --image-type "COS" --zone $CLUSTER_ZONE  \
       --project $GCLOUD_PROJECT&>>gke_k8s.log

