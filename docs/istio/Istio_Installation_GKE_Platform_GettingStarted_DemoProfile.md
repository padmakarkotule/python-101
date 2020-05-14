# Istio Installation on GKE Platform - Getting Started with Demo Profile
Steps follow as per link - https://istio.io/docs/setup/getting-started/
**Objectives**

In this lab, you will learn how to perform the following tasks:

- Provision a cluster on Google Kubernetes Engine (GKE)
- Install and configure the Istio on GKE, which includes the Istio
- control-plane and a method to deploy Envoy proxies as sidecars.
- Deploy demo profile

This guide lets you quickly evaluate Istio. 
These steps require you to have a cluster running a compatible version of Kubernetes.
Follow these steps to get started with Istio:
- Deploy GKE cluster
- Download and install Istio
- Deploy the sample application
- Open the application to outside traffic
- View the dashboard

## Install and configure Google Kubernetes Engine (GKE) 
https://istio.io/docs/setup/platform-setup/gke/

**Use Cloud Shell to deploy your GKE cluster**

1.If you haven't already, open a new Cloud Shell session and run the following 
    to set environment variables for the zone and cluster name:
    
Now **run the following command to create your GKE cluster**
    
    # Initial setup 
    # Run all following commands on Google cloud shell.
    gcloud auth list
    gcloud config list project
    export GCLOUD_PROJECT=$(gcloud config get-value project)
    
    # Kubernetes cluster basic details
    export CLUSTER_NAME=central
    export CLUSTER_ZONE=us-central1-b
    export CLUSTER_VERSION=latest

**The default installation of Istio requires nodes with >1 vCPU. 
If you are installing with the demo configuration profile, you can remove 
the --machine-type argument to use the smaller n1-standard-1 machine size instead.**    

    # gcloud istio demo profile setup (use beta to start add-on)     
    gcloud container clusters create $CLUSTER_NAME \
	    --cluster-version=$CLUSTER_VERSION \
	    --machine-type "n1-standard-2" \
	    --num-nodes 4 \
	    --image-type "COS" \	        
	    --zone $CLUSTER_ZONE  \
        --project $GCLOUD_PROJECT

    # output of above command

	
This command creates a cluster in a single zone, with 4 nodes. 
**The nodes are in the default vpc network.**. The new cluster (central) takes 
several minutes to deploy. You can review your cluster, when deployment is complete, 
**from the   Navigation menu > Kubernetes Engine > Clusters.**

2.Retrieve your credentials for kubectl. 
   Once your cluster has been created, configure kubectl command line access by 
   running the following: 


    export GCLOUD_PROJECT=$(gcloud config get-value project)
    
    gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $CLUSTER_ZONE --project $GCLOUD_PROJECT

    # output
 

3.Grant admin permissions in the cluster to the current gcloud user:
Grant cluster administrator (admin) permissions to the current user. 
To create the necessary RBAC rules for Istio, the current user requires 
admin permissions.

    kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$(gcloud config get-value core/account)

    # Output



**Note: although you can run the demo app without granting cluster admin permissions, 
the permissions are required if you want to access telemetry data and 
other Istio features.**

#### Verify GKE installation

1.Check that your cluster is up and running.

	gcloud container clusters list

    # Output (do not copy)

# Download istio and configure istioctl
1.Use Cloud Shell to download and extract the Istio release, with the istioctl tool, 
    and sample code:
    
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
	
	# from git.io - curl -L https://git.io/getLatestIstio | ISTIO_VERSION=$ISTIO_VERSION sh -
	# from istio.io with latest version - curl -L https://istio.io/downloadIstio | sh -
	# download a specific version
	
	curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.5.2 sh -
	
	# Output
    

2.Move to the Istio package directory. For example, if the package is istio-1.5.2

    cd istio-1.5.2

The installation directory contains:

    Installation YAML files for Kubernetes in install/kubernetes
    Sample applications in samples/
    The istioctl client binary in the bin/ directory.

3.Add the istioctl client to your path (Linux or macOS):

    cd ./istio-*
    export PATH=$PWD/bin:$PATH
    ls -al
    
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

## Install Istio

1.For this installation, we use the demo configuration profile. It’s selected to 
have a good set of defaults for testing, but there are other profiles for 
production or performance testing.

    istioctl manifest apply --set profile=demo
    
    # Output
    
    
2.Add a namespace label to instruct Istio to automatically inject 
Envoy sidecar proxies **when you deploy your application later:**

    kubectl label namespace default istio-injection=enabled
    
    # Output
    
### Verify Istio installation

1.Ensure the following Kubernetes services are deployed: 
  istio-citadel, istio-galley, istio-pilot, istio-ingressgateway, 
  istio-policy, istio-sidecar-injector, and istio-telemetry. 
  You'll also see other deployed services:

    kubectl get service -n istio-system

    #Output 

   
2.Ensure the corresponding Kubernetes pods are deployed and all 
containers are up and running:     
istio-pilot-, istio-galley-, istio-policy-, istio-telemetry-, istio-ingressgateway-, 
istio-sidecar-injector-, and istio-citadel-.
    
    kubectl get pods -n istio-system

    # Output, 

    
## Deploy the sample application

1.Deploy the Bookinfo sample application:

     kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
     
     # Output
     
2.The application will start. As each pod becomes ready, 
  **the Istio sidecar will deploy along with it.**

    kubectl get services
    
    # Output       
    
    and
    kubectl get pods
     
    # Output
    
Note:- Re-run the previous command and wait until all pods report READY 2 / 2 and 
STATUS Running before you go to the next step. This might take a few 
minutes depending on your platform.   

3.Verify everything is working correctly up to this point. Run this command to 
see if the app is running inside the cluster and serving HTML pages by 
checking for the page title in the response:

    kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"
    <title>Simple Bookstore App</title>

    # Output
    
### Open the application to outside traffic (Ingress Gateway)    
The Bookinfo application is deployed but not accessible from the outside. To make 
it accessible, you need to create an Istio Ingress Gateway, which maps a 
path to a route at the edge of your mesh.

1.Associate this application with the Istio gateway:

    kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
    
    # Output
    
2.Confirm the gateway has been created:

    kubectl get gateway
    
    # Output

### Determining the ingress IP and ports

Follow these instructions to set the INGRESS_HOST and INGRESS_PORT variables 
for accessing the gateway. Use the tabs to choose the instructions for 
your chosen platform:

    kubectl get svc istio-ingressgateway -n istio-system
    
    # Output
    
Set the ingress IP and ports: (If have load balancing)

     export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
     export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
     export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
     
### Set the firewall rules
You need to create firewall rules to allow the TCP traffic to the 
ingressgateway service’s ports. Run the following commands to allow the 
traffic for the HTTP port, the secure port (HTTPS) or both:  

     gcloud compute firewall-rules create allow-gateway-http --allow tcp:$INGRESS_PORT
     gcloud compute firewall-rules create allow-gateway-https --allow tcp:$SECURE_INGRESS_PORT
     
1.Set GATEWAY_URL: 

    export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
2.Ensure an IP address and port were successfully assigned to the environment variable:

    echo $GATEWAY_URL
    
### Verify external access    
Confirm that the Bookinfo application is accessible from outside. Copy the 
output of this command and paste into your browser:

    echo http://$GATEWAY_URL/productpage
    
# View the dashboard (Kiali)
Istio has several optional dashboards installed by the demo installation. 
The Kiali dashboard helps you understand the structure of your service mesh 
by displaying the topology and indicates the health of your mesh.

1.Access the Kiali dashboard. The default user name is admin and default password is admin.

    istioctl dashboard kiali
    
2.In the left navigation menu, select Graph and in the Namespace drop down, select 
default. The Kiali dashboard shows an overview of your mesh with the relationships 
between the services in the Bookinfo sample application. It also provides filters 
to visualize the traffic flow.

## Accessing The Kiali Service
Ref. Link - https://www.magalix.com/blog/working-with-istio-track-your-services-with-kiali

Since Kiali is, by default, an internal service, you can access it in either of two ways:

**Using port forwarding**

    kubectl -n istio-system port-forward svc/kiali  20001:20001
    
**Convert the service to LoadBalancer**

    kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system
    
    # Then get the IP address and port:
    kubectl -n istio-system get service kiali -o jsonpath='{.status.loadBalancer.ingress[0].ip}
    kubectl -n istio-system get service kiali -o jsonpath='{.spec.ports[?(@.name=="http-kiali")].port}'    

Navigate to the Kiali URL 

    for example, http://<Kiali-load-balance-IP>:20001/kiali/
    http://52.150.35.253:20001/kiali/
    you should see a page similar to the following:





# Next steps

These tasks are a great place for beginners to further evaluate 
Istio’s features using this demo installation:

- Request routing
- Fault injection
- Traffic shifting
- Querying metrics
- Visualizing metrics
- Rate limiting
- Accessing external services
- Visualizing your mesh


# Uninstall

The uninstall deletes the RBAC permissions, the istio-system namespace, and all resources.

    istioctl manifest generate --set profile=demo | kubectl delete -f -
    
    To delete the Bookinfo sample application and its configuration, see Bookinfo cleanup.
 
  