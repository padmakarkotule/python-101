# Istio Installation using GKE Add-On
**Objectives**

In this lab, you will learn how to perform the following tasks:

- Provision a cluster on Google Kubernetes Engine (GKE)
- Install and configure the Istio on GKE Add-On, which includes the Istio
- control-plane and a method to deploy Envoy proxies as sidecars.

Istio on GKE is an add-on for GKE that lets you quickly create a cluster with 
all the components you need to create and run an Istio service mesh, in a single step.

Once installed, your Istio control plane components are automatically kept up-to-date, 
with no need for you to worry about upgrading to new versions. 

**You can also use the add-on to install Istio on an existing cluster.**
For more information, pl. visit https://cloud.google.com/istio/docs/istio-on-gke/overview


## Install and configure a cluster with the Istio on GKE Add-On

In this lab, you'll use a Google Kubernetes Engine (GKE) cluster named central, 
in the us-central1 region. In this task, you:

    •	Deploy the central cluster on GKE using Cloud Shell
    •	Deploy a service mesh using the Istio on GKE add-on.

### Use Cloud Shell to deploy your GKE cluster with Istio

1.	If you haven't already, open a new Cloud Shell session and run the following 
    to set environment variables for the zone and cluster name:
    
Now **run the following command to create your GKE cluster using the Istio on 
    GKE add-on:**
**Add-on options are beta options, so use only demo purpose.** 
    
    # Initial setup 
    # Run all following commands on Google cloud shell.
    gcloud auth list
    gcloud config list project
    export GCLOUD_PROJECT=$(gcloud config get-value project)
    
    # Kubernetes cluster basic details
    export CLUSTER_NAME=central
    export CLUSTER_ZONE=us-central1-b
    export CLUSTER_VERSION=latest

**Using beta and --addons option (As per Qwiklabs)**
    
    # gcloud istio demo profile setup (use beta to start add-on)     
    gcloud beta container clusters create $CLUSTER_NAME \
	    --zone $CLUSTER_ZONE --num-nodes 4 \
	    --machine-type "n1-standard-2" --image-type "COS" \
	    --cluster-version=$CLUSTER_VERSION \
	    --enable-stackdriver-kubernetes \
	    --scopes "gke-default","compute-rw" \
	    --enable-autoscaling --min-nodes 4 --max-nodes 8 \
	    --enable-basic-auth \
	    --addons=Istio --istio-config=auth=MTLS_STRICT

    # output of above command
    WARNING: Currently VPC-native is not the default mode during cluster creation. In the future, this will become the default mode and can be disabled using `--no-enable-ip-alias` flag. Use `--[no-]enable-ip-alias` flag to suppress this warning.
    WARNING: Newly created clusters and node-pools will have node auto-upgrade enabled by default. This can be disabled using the `--no-enable-autoupgrade` flag.
    WARNING: Starting with version 1.18, clusters will have shielded GKE nodes by default.
    WARNING: Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most 1008 node(s).
    This will enable the autorepair feature for nodes. Please see https://cloud.google.com/kubernetes-engine/docs/node-auto-repair for more information on node autorepairs.
    Creating cluster central in us-central1-b... Cluster is being health-checked...⠶   
    Created [https://container.googleapis.com/v1beta1/projects/devops-padmakar/zones/us-central1-b/clusters/central].
    To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-central1-b/central?project=devops-padmakar
    kubeconfig entry generated for central.
    NAME     LOCATION       MASTER_VERSION  MASTER_IP      MACHINE_TYPE   NODE_VERSION    NUM_NODES  STATUS
    central  us-central1-b  1.15.11-gke.12  35.225.138.25  n1-standard-2  1.15.11-gke.12  4          RUNNING
    padmakar_kotule@cloudshell:~ (devops-padmakar)$
	
This command creates a cluster in a single zone, with 4 nodes, that can scale up to 8 
nodes. **The nodes are in the default vpc network.** Stackdriver Kubernetes Engine 
Monitoring is enabled, which you will see later. The new cluster (central) takes 
several minutes to deploy. You can review your cluster, when deployment is complete, 
**from the   Navigation menu > Kubernetes Engine > Clusters.**

2. Once your cluster has been created, configure kubectl command line access by 
   running the following: 


    export GCLOUD_PROJECT=$(gcloud config get-value project)
    gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $CLUSTER_ZONE --project $GCLOUD_PROJECT

    # output
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ export GCLOUD_PROJECT=$(gcloud config get-value project)
    Your active configuration is: [cloudshell-30942]
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ gcloud container clusters get-credentials $CLUSTER_NAME \
    >     --zone $CLUSTER_ZONE --project $GCLOUD_PROJECT
    Fetching cluster endpoint and auth data.
    kubeconfig entry generated for central.

7. Grant admin permissions in the cluster to the current gcloud user:


    kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$(gcloud config get-value core/account)

    # Output
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ kubectl create clusterrolebinding cluster-admin-binding \
    >     --clusterrole=cluster-admin \
    >     --user=$(gcloud config get-value core/account)
    Your active configuration is: [cloudshell-30942]
    clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-binding created
    padmakar_kotule@cloudshell:~ (devops-padmakar)$


**Note: although you can run the demo app without granting cluster admin permissions, 
the permissions are required if you want to access telemetry data and 
other Istio features.**

### Verify installation

1.Check that your cluster is up and running.

	gcloud container clusters list

    # Output (do not copy)
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ gcloud container clusters list
    NAME     LOCATION       MASTER_VERSION  MASTER_IP      MACHINE_TYPE   NODE_VERSION    NUM_NODES  STATUS
    central  us-central1-b  1.15.11-gke.12  35.225.138.25  n1-standard-2  1.15.11-gke.12  4          RUNNING
    padmakar_kotule@cloudshell:~ (devops-padmakar)$

2.Ensure the following Kubernetes services are deployed: 
  istio-citadel, istio-galley, istio-pilot, istio-ingressgateway, 
  istio-policy, istio-sidecar-injector, and istio-telemetry. 
  You'll also see other deployed services:

    kubectl get service -n istio-system

    #Output 
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ kubectl get service -n istio-system
    NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                                                                                                                                      AGE
    istio-citadel            ClusterIP      10.43.255.115   <none>          8060/TCP,15014/TCP                                                                                                                           10m
    istio-galley             ClusterIP      10.43.244.6     <none>          443/TCP,15014/TCP,9901/TCP                                                                                                                   10m
    istio-ingressgateway     LoadBalancer   10.43.253.96    35.232.147.32   15020:30446/TCP,80:31877/TCP,443:32295/TCP,31400:30703/TCP,15029:30765/TCP,15030:30702/TCP,15031:32486/TCP,15032:30904/TCP,15443:31887/TCP   10m
    istio-pilot              ClusterIP      10.43.255.5     <none>          15010/TCP,15011/TCP,8080/TCP,15014/TCP                                                                                                       10m
    istio-policy             ClusterIP      10.43.250.116   <none>          9091/TCP,15004/TCP,15014/TCP                                                                                                                 10m
    istio-sidecar-injector   ClusterIP      10.43.251.165   <none>          443/TCP                                                                                                                                      10m
    istio-telemetry          ClusterIP      10.43.250.205   <none>          9091/TCP,15004/TCP,15014/TCP,42422/TCP                                                                                                       10m
    promsd                   ClusterIP      10.43.240.42    <none>          9090/TCP                                                                                                                                     10m
    padmakar_kotule@cloudshell:~ (devops-padmakar)$
   
3.Ensure the corresponding Kubernetes pods are deployed and all 
containers are up and running:     
istio-pilot-, istio-galley-, istio-policy-, istio-telemetry-, istio-ingressgateway-, 
istio-sidecar-injector-, and istio-citadel-.
    
    kubectl get pods -n istio-system

    # Output, 
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ kubectl get pods -n istio-system
    NAME                                             READY   STATUS      RESTARTS   AGE
    istio-citadel-77cd449c7-zhmzt                    1/1     Running     0          14m
    istio-galley-56d758c767-zx5bk                    1/1     Running     0          14m
    istio-ingressgateway-575998658f-7s4dr            1/1     Running     0          14m
    istio-pilot-7ccf6df767-jpm6s                     2/2     Running     0          14m
    istio-policy-6c9c989cb4-5pwcd                    2/2     Running     1          14m
    istio-security-post-install-1.2.10-gke.3-nmj65   0/1     Completed   0          14m
    istio-sidecar-injector-74945d98c7-sfqg2          1/1     Running     0          14m
    istio-telemetry-5649444d-wgxd6                   2/2     Running     2          14m
    promsd-66fc944cd-zqgmh                           2/2     Running     1          14m
    padmakar_kotule@cloudshell:~ (devops-padmakar)$

## Download and configure istioctl
1.	Use Cloud Shell to download and extract the Istio release, with the istioctl tool, 
    and sample code: (Note in actual lab ISTIO_VERSION used as 1.2.2)
    but duing actual lab, entered latest istio version e.g. 1.5.2
    
    export LAB_DIR=$HOME/bookinfo-lab
    export ISTIO_VERSION=1.5.2	
	mkdir $LAB_DIR
	cd $LAB_DIR
	
	# Output
	padmakar_kotule@cloudshell:~ (devops-padmakar)$ export ISTIO_VERSION=1.5.2
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ mkdir $LAB_DIR
    padmakar_kotule@cloudshell:~ (devops-padmakar)$ cd $LAB_DIR
    padmakar_kotule@cloudshell:~/bookinfo-lab (devops-padmakar)$ pwd
    /home/padmakar_kotule/bookinfo-lab
	
	curl -L https://git.io/getLatestIstio | ISTIO_VERSION=$ISTIO_VERSION sh -
	
	# Output
	padmakar_kotule@cloudshell:~/bookinfo-lab (devops-padmakar)$ curl -L https://git.io/getLatestIstio | ISTIO_VERSION=$ISTIO_VERSION sh -
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                   Dload  Upload   Total   Spent    Left  Speed
    0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
    100  3896  100  3896    0     0   2796      0  0:00:01  0:00:01 --:--:--  2796
    Downloading istio-1.5.2 from https://github.com/istio/istio/releases/download/1.5.2/istio-1.5.2-linux.tar.gz ...
    Istio 1.5.2 Download Complete!
    Istio has been successfully downloaded into the istio-1.5.2 folder on your system.
    Next Steps:
    See https://istio.io/docs/setup/kubernetes/install/ to add Istio to your Kubernetes cluster.
    To configure the istioctl client tool for your workstation,
    add the /home/padmakar_kotule/bookinfo-lab/istio-1.5.2/bin directory to your environment path variable with:
             export PATH="$PATH:/home/padmakar_kotule/bookinfo-lab/istio-1.5.2/bin"
    Begin the Istio pre-installation verification check by running:
             istioctl verify-install
    Need more information? Visit https://istio.io/docs/setup/kubernetes/install/
    padmakar_kotule@cloudshell:~/bookinfo-lab (devops-padmakar)$


2.The installation directory contains the following files which we'll use.
- Sample applications in samples/.
- The **istioctl** client binary in the bin/ directory. *
  *Similar to kubectl for Kubernetes**, 
  **this is the tool used to manage Istio, including network routing and security policies.**
- The istio.VERSION configuration file.

3.Make the Istio tools visible to your environment, by adding bin to your PATH:

    cd ./istio-*
    export PATH=$PWD/bin:$PATH
    
    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab (devops-padmakar)$ cd ./istio-1.5.2/
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ export PATH=$PWD/bin:$PATH
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ ls -al
    total 48
    drwxr-x---  6 padmakar_kotule padmakar_kotule  4096 Apr 21 04:21 .
    drwxr-xr-x  3 padmakar_kotule padmakar_kotule  4096 May  8 15:09 ..
    drwxr-x---  2 padmakar_kotule padmakar_kotule  4096 Apr 21 04:21 bin
    drwxr-xr-x  6 padmakar_kotule padmakar_kotule  4096 Apr 21 04:21 install
    -rw-r--r--  1 padmakar_kotule padmakar_kotule 11348 Apr 21 04:21 LICENSE
    -rw-r-----  1 padmakar_kotule padmakar_kotule   595 Apr 21 04:21 manifest.yaml
    -rw-r--r--  1 padmakar_kotule padmakar_kotule  5818 Apr 21 04:21 README.md
    drwxr-xr-x 19 padmakar_kotule padmakar_kotule  4096 Apr 21 04:21 samples
    drwxr-x---  2 padmakar_kotule padmakar_kotule  4096 Apr 21 04:21 tools
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$

4.Verify istioctl works:

    istioctl version
    
    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ istioctl version
    client version: 1.5.2
    control plane version: c834c448a92e691d71b42a966d94fb1822ac10e1-dirty
    data plane version: 1.0-dev (1 proxies)
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$
   
    # outpus when we use ISTIO_VERSION=1.2.2
    version.BuildInfo{Version:"1.2.2", GitRevision:"...", User:"root",
    Host:"...", GolangVersion:"...", DockerHub:"docker.io/istio",
    BuildStatus:"Clean", GitTag:"..."}



##### Error - Example output of all commands 
- Running Kubernetes cluster on GKe with DevOps-Padmakar Project under GSLAB gke account.

**Note: - Error**
Installation
Command (Kubernet cluster creation) -
 
Sample output 
padmakar_kotule@cloudshell:~ (devops-padmakar)$ gcloud beta container clusters create $CLUSTER_NAME     --zone $CLUSTER_ZONE --num-nodes 2     --machine-type "n1-standard-2" --image-type "COS"     --cluster-version=$CLUSTER_VERSION     --enable-stackdriver-kubernetes     --scopes "gke-default","compute-rw"     --enable-basic-auth     --addons=Istio --istio-config=auth=MTLS_STRICT
WARNING: Currently VPC-native is not the default mode during cluster creation. In the future, this will become the default mode and can be disabled using `--no-enable-ip-alias` flag. Use `--[no-]enable-ip-alias` flag to suppress this warning.
WARNING: Newly created clusters and node-pools will have node auto-upgrade enabled by default. This can be disabled using the `--no-enable-autoupgrade` flag.
WARNING: Starting with version 1.18, clusters will have shielded GKE nodes by default.
WARNING: Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most 1008 node(s).
This will enable the autorepair feature for nodes. Please see https://cloud.google.com/kubernetes-engine/docs/node-auto-repair for more information on node autorepairs.
Creating cluster cluster-1 in asia-south1-a... Cluster is being deployed...⠶  


**Demo lab, DevOps-padmakar**
**Istio Getting started - Link https://istio.io/docs/setup/platform-setup/gke/**

	export CLUSTER_NAME=cluster-1
	export CLUSTER_ZONE=asia-south1-b
	export CLUSTER_VERSION=latest
	
	gcloud container clusters create $CLUSTER_NAME \
	    --zone $CLUSTER_ZONE --num-nodes 2 \
	    --machine-type "n1-standard-2" --image-type "COS" \
	    --cluster-version=$CLUSTER_VERSION \
	    --enable-stackdriver-kubernetes \
	    --scopes "gke-default","compute-rw" \
	    --enable-autoscaling --min-nodes 2 --max-nodes 4 \
	    --enable-basic-auth \
	    --addons=Istio --istio-config=auth=MTLS_STRICT
	
	