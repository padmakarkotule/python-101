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

**Jaeger**
Jaeger is open source, end-to-end distributed tracing.
**set the addonComponents.kiali.enabled configuration parameter**
with following command,

    istioctl manifest apply --set addonComponents.kiali.enabled=true
    
    # Output
    
    