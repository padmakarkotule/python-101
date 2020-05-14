# Istio Add-on

To enable add-on's e.g. the Grafana dashboard on top of the default profile, 
Prometheus Kiali and Jaegar, use following steps.

## Graphana - on Istio
Grafana is an open source solution for running data analytics, pulling up metrics 
that make sense of the massive amount of data & to monitor our apps with the 
help of cool customizable dashboards.

**set the addonComponents.grafana.enabled configuration parameter** 
with the following command:

     istioctl manifest apply --set addonComponents.grafana.enabled=true
     
     #Output
     padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$ istioctl manifest apply --set addonComponents.grafana.enabled=true
        - Applying manifest for component Base...
        ✔ Finished applying manifest for component Base.
        - Applying manifest for component Pilot...
        ✔ Finished applying manifest for component Pilot.
          Waiting for resources to become ready...
          Waiting for resources to become ready...
        - Applying manifest for component IngressGateways...
        - Applying manifest for component AddonComponents...
        ✔ Finished applying manifest for component IngressGateways.
        ✔ Finished applying manifest for component AddonComponents.   
        ✔ Installation complete
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$

In general, you can use the --set flag in istioctl as you would with Helm. 
The only difference is you must prefix the setting paths with values. because this 
is the path to the Helm pass-through API in the IstioOperator API.

## Accessing The Grafana Service (Istio System using Grafana)
Ref. Link - https://www.magalix.com/blog/working-with-istio-track-your-services-with-kiali

**Since Grafana is, by default, an internal service, you can access it in either of two ways:**

**1 - Using port forwarding**

    kubectl -n istio-system port-forward svc/grafana  30000:3000
    
**2 - Convert the service to LoadBalancer**

    kubectl patch service grafana --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system

    # Then get the IP address and port:
    kubectl -n istio-system get service grafana -o jsonpath='{.status.loadBalancer.ingress[0].ip}
    kubectl -n istio-system get service grafana -o jsonpath='{.spec.ports[?(@.name=="http-kiali")].port}'    

Navigate to the Grafana URL 

    for example, http://<Grafana-load-balance-IP>:3000/dashboard/db/istio-mesh-dashboard
    http://52.150.35.253:3000/dashboard/db/istio-mesh-dashboard
    you should see a page:

## Prometheus - on Istio
**set the addonComponents.prometheus.enabled configuration parameter**
with following command,

    istioctl manifest apply --set addonComponents.prometheus.enabled=true
    
    # Output 
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$ istioctl manifest apply --set addonComponents.prometheus.enabled=true
    - Applying manifest for component Base...
    ✔ Finished applying manifest for component Base.
    - Applying manifest for component Pilot...
    ✔ Finished applying manifest for component Pilot.
    - Applying manifest for component AddonComponents...
    - Applying manifest for component IngressGateways...
    ✔ Finished applying manifest for component IngressGateways.
    ✔ Finished applying manifest for component AddonComponents.
    ✔ Installation complete
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$

You can also access from console, but need to expose port and then access it.

    istioctl dashboard jaeger
    

## Kiali - on Istio
Kiali is an observability console for Istio with service mesh configuration capabilities.
**set the addonComponents.kiali.enabled configuration parameter**
with following command,

    istioctl manifest apply --set addonComponents.kiali.enabled=true
    
    # Output 
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$ istioctl manifest apply --set addonComponents.kiali.enabled=true
    - Applying manifest for component Base...
    ✔ Finished applying manifest for component Base.
    - Applying manifest for component Pilot...
    ✔ Finished applying manifest for component Pilot.
    - Applying manifest for component AddonComponents...
    - Applying manifest for component IngressGateways...
    ✔ Finished applying manifest for component IngressGateways.
    ✔ Finished applying manifest for component AddonComponents.
    ✔ Installation complete
    padmakar_kotule@cloudshell:~/bookinfo-lab/istio-1.5.2$

## Accessing The Kiali Service
Ref. Link - https://www.magalix.com/blog/working-with-istio-track-your-services-with-kiali

**Since Kiali is, by default, an internal service, you can access it in either of two ways:**

**1 - Using port forwarding**

    kubectl -n istio-system port-forward svc/kiali  20001:20001
    
**2 - Convert the service to LoadBalancer**

    kubectl patch service kiali --patch '{"spec":{"type":"LoadBalancer"}}' -n istio-system
    
    # Then get the IP address and port:
    kubectl -n istio-system get service kiali -o jsonpath='{.status.loadBalancer.ingress[0].ip}
    kubectl -n istio-system get service kiali -o jsonpath='{.spec.ports[?(@.name=="http-kiali")].port}'    

Navigate to the Kiali URL 

    for example, http://<Kiali-load-balance-IP>:20001/kiali/
    http://52.150.35.253:20001/kiali/
    you should see a page:

**Jaeger**
Jaeger is open source, end-to-end distributed tracing.
**set the addonComponents.kiali.enabled configuration parameter**
with following command,

    ## need to check - istioctl manifest apply --set addonComponents.tracing.enabled=true
    
    # Output
    
You can also access from console, but need to expose port and then access it.

    istioctl dashboard jaeger