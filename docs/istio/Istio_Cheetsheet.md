# Istio Installation - - Getting Started with Demo Profile.

## Kubernetes Installation on GKE Platform 

**Install and configure Google Kubernetes Engine (GKE)**

    # Initial setup 
    # Run all following commands on Google cloud shell.
    gcloud auth list
    gcloud config list project
    export GCLOUD_PROJECT=$(gcloud config get-value project)
    
    # Kubernetes cluster basic details
    export CLUSTER_NAME=democluster
    export CLUSTER_ZONE=us-central1-b
    export CLUSTER_VERSION=latest
    
    gcloud container clusters create $CLUSTER_NAME \
	    --cluster-version=$CLUSTER_VERSION \
	    --machine-type "n1-standard-2" \
	    --num-nodes 4 \
	    --image-type "COS" \	        
	    --zone $CLUSTER_ZONE  \
        --project $GCLOUD_PROJECT

**Retrieve your credentials for kubectl.**

    export GCLOUD_PROJECT=$(gcloud config get-value project)
    
    gcloud container clusters get-credentials $CLUSTER_NAME \
    --zone $CLUSTER_ZONE --project $GCLOUD_PROJECT        
    
**Grant admin permissions in the cluster to the current gcloud user**

    kubectl create clusterrolebinding cluster-admin-binding \
    --clusterrole=cluster-admin \
    --user=$(gcloud config get-value core/account)

**Verify GKE installation**

    gcloud container clusters list
    #kubectl get service -n istio-system
    
## Istio Installation on GKE Platform - Getting Started with Demo Profile.

**Download install istio and configure istioctl**    

    export LAB_DIR=$HOME/bookinfo-lab
    export ISTIO_VERSION=1.5.2	
	mkdir $LAB_DIR
	cd $LAB_DIR
	
	curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.5.2 sh -
	
	cd istio-1.5.2
	cd ./istio-*
    export PATH=$PWD/bin:$PATH
    ls -al   
    istioctl version
 
    
    # Install Istio
    istioctl manifest apply --set profile=demo
    
    # Add a namespace label to instruct Istio to automatically inject 
    # Envoy sidecar proxies **when you deploy your application later:**

    kubectl label namespace default istio-injection=enabled
    
    # Verify install
    istioctl version
    istioctl verify-install
    
**Verify Istio installation**    

    kubectl get service -n istio-system
    kubectl get pods -n istio-system
    
## Deploy the sample application

    # Deploy application
    kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
    # Verify services
    kubectl get services
    
    #Note:- Re-run the previous command and wait until all pods report READY 2 / 2
    
    # Verify app is running
    kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"
    <title>Simple Bookstore App</title>
    
## Igress Gateway - Open the application to outside traffic.

    # Associate application with Istio Gateway
    kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
       
    # Verify gateway is created
    kubectl get gateway
    
    # Determining the ingress IP and ports   
    kubectl get svc istio-ingressgateway -n istio-system
    
    # Set the ingress IP and ports: (If have load balancing) 
    
    export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
    export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
     
    # Set the firewall rules
    
    gcloud compute firewall-rules create allow-gateway-http --allow tcp:$INGRESS_PORT
    gcloud compute firewall-rules create allow-gateway-https --allow tcp:$SECURE_INGRESS_PORT
  
    # Set GATEWAY URL
    export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT    
    
    # Verify external access #Access url from browser
    http://$GATEWAY_URL/productpage

# View Dashboard with Prometheus, Graphana, Kiali, Jaeger
**Since Prometheus, Graphana, Kiali and Jaeger by default running as an internal services,
 you can access it in either of two ways:**
**1 - Using port forwarding**  Or **2 - Convert the service to LoadBalancer**
**Note - Here we are exposing Prometheus, Graphana, Kiali and Jaeger using 
with LoadBalancer.**

- Prometheus - http://<External IP e.g. 34.71.126.82>:9090/
- Graphana - http://<External IP e.g. 34.71.126.82>:3000/
    http://34.71.126.82:3000/dashboard/db/istio-service-dashboard
    http://34.71.126.82:3000/dashboard/db/istio-mesh-dashboard
    http://34.71.126.82:3000/dashboard/db/istio-workload-dashboard
- Kiali - http://<External IP e.g. 34.71.126.82>:20001/kiali/
- Jaeger - http://<External IP e.g. 34.71.126.82>:16686/

**Prometheus**
    **set the addonComponents.prometheus.enabled configuration parameter**
with following command,

    # Enable addon component Prometheus and access using web.
    istioctl manifest apply --set addonComponents.prometheus.enabled=true    
    kubectl patch service prometheus --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system
    # Access prometheus example, http://<Prometheus-load-balance-IP>:3
    http://34.71.126.82:9090
    
   
**Graphana**
    **set the addonComponents.prometheus.enabled configuration parameter**
with following command,

    # Enable addon component Graphana and access using web.
    istioctl manifest apply --set addonComponents.grafana.enabled=true    
    kubectl patch service grafana --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

Navigate to the Grafana URL
istio-mesh-dashboard
    # example, http://<Grafana-load-balance-IP>:3000/dashboard/db/istio-mesh-dashboard
    http://34.71.126.82:3000/dashboard/db/istio-mesh-dashboard
    # There are different dashboards, for more details pl. visit, 
    # https://istio.io/docs/tasks/observability/metrics/using-istio-dashboard/

Services dashboard e.g.
    http://localhost:3000/dashboard/db/istio-service-dashboard 
    e.g.
    http://34.71.126.82:3000/dashboard/db/istio-service-dashboard

Visualize Workload Dashboards
    http://localhost:3000/dashboard/db/istio-workload-dashboard
    http://34.71.126.82:3000/dashboard/db/istio-workload-dashboard 
Examples,
http://34.71.126.82:3000/dashboard/db/istio-service-dashboard
http://34.71.126.82:3000/dashboard/db/istio-mesh-dashboard
http://34.71.126.82:3000/dashboard/db/istio-workload-dashboard

**Kiali**
    **set the addonComponents.prometheus.enabled configuration parameter**
with following command,

    # Enable addon component Kiali and access it using web.
    istioctl manifest apply --set addonComponents.kiali.enabled=true    
    kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

Navigate to the Kiali URL 
    for example, http://<Kiali-load-balance-IP>:20001/kiali/
    http://52.150.35.253:20001/kiali/

**Jaeger**
    **set the addonComponents.prometheus.enabled configuration parameter**
with following command,

    # First enable tracing if not already or check it. 
    istioctl manifest apply --set addonComponents.tracing.enabled=true
    # Enable addon component Jaeger-query and access using web.
    istioctl manifest apply --set addonComponents.jaeger-query.enabled=true    
    kubectl patch service jaeger-query --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system
    
Navigate to the Jaeger URL 
    http://104.155.149.65:16686   

#######==============Old Output ===============#######
##  View the dashboard Kiali, Prometheus, Graphaha, Jaeger    
    
    # Access the Kiali dashboard.
    istioctl dashboard kiali
    
    # .In the left navigation menu, select Graph and in the Namespace drop down, select 
    default. The Kiali dashboard shows an overview of your mesh with the relationships 
    between the services in the Bookinfo sample application. It also provides filters 
    to visualize the traffic flow.
    
    
## Accessing dashboard jaeger

    istioctl dashboard jaeger
    
## Visualizing Metrics with Grafana

1.Verify that the prometheus service is running in your cluster.
  In Kubernetes environments, execute the following command:
  
    kubectl -n istio-system get svc prometheus
    
2.Verify that the Grafana service is running in your cluster.

    kubectl -n istio-system get svc grafana
    
3.Open the Istio Dashboard via the Grafana UI.
  In Kubernetes environments, execute the following command:
  
    kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000 &

4.Visit http://localhost:3000/dashboard/db/istio-mesh-dashboard in your web browser.

**Note - If error shows as port already in use, then use different port.**
Also this is workaround as running by port forwarding, will need to expose port to access 
from outside.
