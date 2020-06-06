#!/bin/bash

export LAB_DIR=$HOME/istio
mkdir $LAB_DIR
cd $LAB_DIR
cd ./istio-*
export PATH=$PWD/bin:$PATH


# Enable addon of prometheus, grafana, kiali, jaeger
# Note - By-default demo profile of istio enebale prometheus, grafana, kiali and jaeger-query.
# So we don't need to execute following commands.
# But if you use default istio profie (for porduction setup) then you need to enable addon manually.
# following commands will be useful to enable addons.

echo "Enable addon component Prometheus"
#istioctl manifest apply --set addonComponents.prometheus.enabled=true

echo "Enable addon component Graphana"
#istioctl manifest apply --set addonComponents.grafana.enabled=true

echo "Enable addon component Kiali"
#istioctl manifest apply --set addonComponents.kiali.enabled=true

echo "Enable addon component jaeger-query"
#istioctl manifest apply --set addonComponents.jaeger-query.enabled=true