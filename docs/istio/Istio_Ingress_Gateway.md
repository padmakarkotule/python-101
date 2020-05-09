# Enable external access using an Istio Ingress Gateway

Once application example, Bookinfo services are up and running.

**you need to make the application accessible from outside of your Kubernetes cluster**, 
e.g. from a browser. 

An Istio Gateway is used for this purpose.

1.Look at the .yaml which describes the configuration for the application ingress gateway:

    cat samples/bookinfo/networking/bookinfo-gateway.yaml
    
    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ cat samples/bookinfo/networking/bookinfo-gateway.yaml
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: bookinfo-gateway
    spec:
      selector:
        istio: ingressgateway # use istio default controller
      servers:
      - port:
          number: 80
          name: http
          protocol: HTTP
        hosts:
        - "*"
    ---
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: bookinfo
    spec:
      hosts:
      - "*"
      gateways:
      - bookinfo-gateway
      http:
      - match:
        - uri:
            exact: /productpage
        - uri:
            prefix: /static
        - uri:
            exact: /login
        - uri:
            exact: /logout
        - uri:
            prefix: /api/v1/products
        route:
        - destination:
            host: productpage
            port:
              number: 9080
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$
     
Look for the **Gateway and VirtualService mesh resources** which get deployed. 
The Gateway exposes services to users outside the service mesh, and allows Istio 
features such as monitoring and route rules to be applied to traffic entering 
the cluster.

2.Configure the ingress gateway for the application, which exposes an external IP you 
  will use later:

    kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml

    # Output
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$ kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
    
    gateway.networking.istio.io/bookinfo-gateway created
    virtualservice.networking.istio.io/bookinfo created
    
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2 (devops-padmakar)$
