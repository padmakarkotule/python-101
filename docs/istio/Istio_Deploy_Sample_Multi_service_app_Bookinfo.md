# Deploy Sample an Istio-enabled Multi service application - Bookinfo

In this task, **you enable the istioctl tool**, set up the Bookinfo sample microservices 
application, and explore the app.

## Bookinfo Overview

After Istio installation and configuraiton, and verified, you can deploy one of the 
sample applications provided with the installation — BookInfo. 
This is a simple mock bookstore application made up of four microservices - all managed 
using Istio. Each microservice is written in a different language, to demonstrate how 
you can use Istio in a multi-language environment, without any changes to code.

The microservices are:
- productpage: calls the details and reviews microservices to populate the page.
- details: contains book information.
- reviews: contains book reviews. It also calls the ratings microservice.
- ratings: contains book ranking information that accompanies a book review.

There are 3 versions of the reviews microservice:
- Reviews v1 doesn't call the ratings service.
- Reviews v2 calls the ratings service, and displays each rating as 1 - 5 black stars.
- Reviews v3 calls the ratings service, and displays each rating as 1 - 5 red stars.
The end-to-end architecture of the application looks like this:

Link - Image of 

You can find the source code and all the other files used in this example in your 
Istio samples/bookinfo directory.
Link - https://github.com/istio/istio/tree/master/samples/bookinfo

## Deploy Bookinfo

1.Look at the .yaml which describes the bookInfo application:

    cat samples/bookinfo/platform/kube/bookinfo.yaml
    Look for containers to see that each Deployment, has one container, for each 
    version of each service in the Bookinfo application.
    
    # Output
    
    # Copyright 2017 Istio Authors
    #
    #   Licensed under the Apache License, Version 2.0 (the "License");
    #   you may not use this file except in compliance with the License.
    #   You may obtain a copy of the License at
    #
    #       http://www.apache.org/licenses/LICENSE-2.0
    #
    #   Unless required by applicable law or agreed to in writing, software
    #   distributed under the License is distributed on an "AS IS" BASIS,
    #   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    #   See the License for the specific language governing permissions and
    #   limitations under the License.
    
    ##################################################################################################
    # This file defines the services, service accounts, and deployments for the Bookinfo sample.
    #
    # To apply all 4 Bookinfo services, their corresponding service accounts, and deployments:
    #
    #   kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
    #
    # Alternatively, you can deploy any resource separately:
    #
    #   kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml -l service=reviews # reviews Service
    #   kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml -l account=reviews # reviews ServiceAccount
    #   kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml -l app=reviews,version=v3 # reviews-v3 Deployment
    ##################################################################################################
    # Details service
    ##################################################################################################
    apiVersion: v1
    kind: Service
    metadata:
      name: details
      labels:
        app: details
        service: details
    spec:
      ports:
      - port: 9080
        name: http
      selector:
        app: details
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: bookinfo-details
      labels:
        account: details
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: details-v1
    labels:
    app: details
    version: v1
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: details
          version: v1
      template:
        metadata:
          labels:
            app: details
            version: v1
        spec:
          serviceAccountName: bookinfo-details
          containers:
          - name: details
            image: docker.io/istio/examples-bookinfo-details-v1:1.15.0
            imagePullPolicy: IfNotPresent
            ports:
            - containerPort: 9080
    ---
    ###################################################################################
    # Ratings service
    ###################################################################################
    ...
    ##################################################################################
    # Reviews service
    ##################################################################################
    ...
    ---
    #################################################################################
    # Productpage services
    ##############################################
    ...
       
2.Look at the same .yaml with Istio proxy sidecars injected using istioctl:

    istioctl kube-inject -f samples/bookinfo/platform/kube/bookinfo.yaml
    
    # Output
    
    #############################################################
    # Details service
    #############################################################
    apiVersion: v1
    kind: Service
    metadata:
      name: details
      labels:
        app: details
        service: details
    spec:
      ports:
      - port: 9080
        name: http
      selector:
        app: details
    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: bookinfo-details
      labels:
        account: details
    ---
    apiVersion: apps/v1
    kind: Deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: details
          version: v1
      strategy: {}
      template:
        metadata:
          annotations:
            sidecar.istio.io/status: '{"version":"249fe8117967ad89e644f4ee6f775cd76fc32e399ad4faecc9541b9277053d85","initContainers":["istio-init"],"containers":["istio-proxy"],"volumes":["istio-envoy","istio-certs"],"imagePullSecrets":null}'
          creationTimestamp: null
          labels:
            app: details
            security.istio.io/tlsMode: istio
            version: v1
        spec:
          containers:
          - image: docker.io/istio/examples-bookinfo-details-v1:1.15.0
            imagePullPolicy: IfNotPresent
            name: details
            ports:
            - containerPort: 9080
            resources: {}
          - args:
    
  **Now, when you scroll up, and look for containers, you can see extra configuration 
  describing the proxy sidecar containers that will be deployed.**
  
  **istioctl kube-inject takes a Kubernetes YAML file as input, and outputs a version of 
  that YAML which includes the Istio proxy.** 
  
  **You can look at one of the Deployments 
  in the output from istio kube-inject. It includes a second container, 
  the Istio sidecar, along with all the configuration necessary.**


3.In Cloud Shell, use the following command to inject the proxy sidecar along 
with each application Pod that is deployed.   
Istio uses an extended version of the open-source Envoy proxy, a high-performance proxy 
developed in C++, to mediate all inbound and outbound traffic for all services 
in the service mesh. Istio leverages Envoy's many built-in features including,
dynamic service discovery, load balancing, TLS termination, HTTP/2 & gRPC proxying, 
circuit breakers, health checks, staged rollouts with %-based traffic split, 
fault injection, and rich metrics.

    kubectl apply -f <(istioctl kube-inject -f samples/bookinfo/platform/kube/bookinfo.yaml)
    
    #Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)
    $ kubectl apply -f <(istioctl kube-inject -f samples/bookinfo/platform/kube/bookinfo.yaml)
    service/details created
    serviceaccount/bookinfo-details created
    deployment.apps/details-v1 created
    service/ratings created
    serviceaccount/bookinfo-ratings created
    deployment.apps/ratings-v1 created
    service/reviews created
    serviceaccount/bookinfo-reviews created
    deployment.apps/reviews-v1 created
    deployment.apps/reviews-v2 created
    deployment.apps/reviews-v3 created
    service/productpage created
    serviceaccount/bookinfo-productpage created
    deployment.apps/productpage-v1 created
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$

Note: Automatic sidecar injection can be enabled by labeling the namespace 
hosting the application with istio-injection=enabled, using a 
command like: 

    kubectl label namespace default istio-injection=enabled
    
    # Output
    

## Enable external access using an Istio Ingress Gateway 
Once application example, Bookinfo services are up and running.

**you need to make the application accessible from outside of your Kubernetes cluster**, 
e.g. from a browser. 

An Istio Gateway is used for this purpose.

1.Look at the .yaml which describes the configuration for the application ingress gateway:
2.cat samples/bookinfo/networking/bookinfo-gateway.yaml
  Look for the Gateway and VirtualService mesh resources which get deployed. 
  The Gateway exposes services to users outside the service mesh, and allows Istio 
  features such as monitoring and route rules to be applied to traffic entering 
  the cluster.
3.Configure the ingress gateway for the application, which exposes an external IP you 
  will use later:
4.kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml

    Example Output
    gateway.networking.istio.io/bookinfo-gateway created
    virtualservice.networking.istio.io/bookinfo created
## Deploy Istio_Ingress Gateway
Link - 

## Verify installation
Verify the Bookinfo deployments
1.Confirm that the application has been deployed correctly, review services, pods, 
  and the ingress gateway:
    
    kubectl get services

    #Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl get services
    NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    details       ClusterIP   10.43.250.37    <none>        9080/TCP   22m
    kubernetes    ClusterIP   10.43.240.1     <none>        443/TCP    111m
    productpage   ClusterIP   10.43.246.173   <none>        9080/TCP   22m
    ratings       ClusterIP   10.43.241.248   <none>        9080/TCP   22m
    reviews       ClusterIP   10.43.251.23    <none>        9080/TCP   22m
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$

2.Review running application pods:

    kubectl get pods

    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl get pods
    NAME                              READY   STATUS    RESTARTS   AGE
    details-v1-fb8bfff8b-ppl2p        2/2     Running   0          24m
    productpage-v1-56bd586b5c-nlcmj   2/2     Running   0          24m
    ratings-v1-f6f4f9994-4l26p        2/2     Running   0          24m
    reviews-v1-56b6c6dd5d-85nj8       2/2     Running   0          24m
    reviews-v2-6457f9b477-t5gm2       2/2     Running   0          24m
    reviews-v3-cb6df6676-6qvhz        2/2     Running   0          24m
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$

You may need to re-run this command until you see that all six pods are in Running status.
**Note: See how each pod has two containers?** 
That's the application container and the Istio proxy sidecar.

3.Confirm that the Bookinfo application is running by sending a curl request 
  to it from some pod, within the cluster, for example from ratings:

    kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') \
    -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"

    #Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl exec -it $(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}') \
    >     -c ratings -- curl productpage:9080/productpage | grep -o "<title>.*</title>"
    
    <title>Simple Bookstore App</title>
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$  
    
4.Confirm the ingress gateway has been created:

    kubectl get gateway

    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl get gateway
    NAME               AGE
    bookinfo-gateway   9m53s
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$
    
5.Get the external IP address of the ingress gateway:

    kubectl get svc istio-ingressgateway -n istio-system
    
    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl get svc istio-ingressgateway -n istio-system
    NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)                                                                                                                                      AGE
    istio-ingressgateway   LoadBalancer   10.43.253.96   35.232.147.32   15020:30446/TCP,80:31877/TCP,443:32295/TCP,31400:30703/TCP,15029:30765/TCP,15030:30702/TCP,15031:32486/TCP,15032:30904/TCP,15443:31887/TCP   115m
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$
    
    # External-IP - 35.232.147.32

6.Check that the Bookinfo app is running by sending a curl request to it from 
  outside the cluster (be sure to update [EXTERNAL-IP] with the output from the 
  previous command):

    export GATEWAY_URL=[EXTERNAL-IP]
	curl -I http://${GATEWAY_URL}/productpage
    
    #Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ curl -I http://${GATEWAY_URL}/productpage
        HTTP/1.1 200 OK
        content-type: text/html; charset=utf-8
        content-length: 5179
        server: istio-envoy
        date: Fri, 08 May 2020 11:10:47 GMT
        x-envoy-upstream-service-time: 1446
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$

## Use the Bookinfo application
After deployment Istio-enabled application. Next, let's see the BookInfo application 
in action.

1.Point your browser to http://[$GATEWAY_URL]/productpage to see the BookInfo 
  web page. Don't forget to replace [$GATEWAY_URL] with your working external IP address.
  Example,
  Link - Image

2.Refresh the page several times.
Notice how you see three different versions of reviews, since we have not yet used 
Istio to control the version routing.
There are three different book review services being called in a round-robin style:
    - No stars
    - Black stars
    - Red stars
Switching among the three is normal Kubernetes routing/balancing behavior.


###### ==========================================================
Ref. From installation steps
## Download and configure istioctl
1.	Use Cloud Shell to download and extract the Istio release, with the istioctl tool, 
    and sample code:
    
    export LAB_DIR=$HOME/bookinfo-lab
    export ISTIO_VERSION=1.2.2	
	mkdir $LAB_DIR
	cd $LAB_DIR
	curl -L https://git.io/getLatestIstio | ISTIO_VERSION=$ISTIO_VERSION sh -

The installation directory contains the following files which we'll use:
- Sample applications in samples/.
- The **istioctl** client binary in the bin/ directory. **Similar to kubectl for Kubernetes**, 
  **this is the tool used to manage Istio, including network routing and security policies.**
- The istio.VERSION configuration file.

2.Make the Istio tools visible to your environment, by adding bin to your PATH:

    cd ./istio-*
    export PATH=$PWD/bin:$PATH

3.Verify istioctl works:

    istioctl version
    E.g. Output
    version.BuildInfo{Version:"1.2.2", GitRevision:"...", User:"root",
    Host:"...", GolangVersion:"...", DockerHub:"docker.io/istio",
    BuildStatus:"Clean", GitTag:"..."}

