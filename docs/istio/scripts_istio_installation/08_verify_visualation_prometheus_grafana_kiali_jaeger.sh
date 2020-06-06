#!/bin/bash
# Verify Prometheus
# Note in query you can type container_cpu_system_seconds_total just for test and click on Graph.
http://34.67.45.214:9090/

# Verify Grafana
http://35.226.246.110:3000/dashboard/db/istio-service-dashboard
http://35.226.246.110:3000/dashboard/db/istio-mesh-dashboard
http://35.226.246.110:3000/dashboard/db/istio-workload-dashboard

# Verify using Kiali
http://34.67.137.217:20001/kiali

# Verify using jaeger-query
http://34.68.153.151:16686