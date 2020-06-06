#!/bin/bash

echo "Execute all steps given in this script manually."
#**Create a secret in your Istio namespace with the credentials that you use to
#authenticate to Kiali.**
#First, define the credentials you want to use as the Kiali username and passphrase.

#- Enter a Kiali username when prompted:
KIALI_USERNAME=$(read -p 'Kiali Username: ' uval && echo -n $uval | base64)

#- Enter a Kiali passphrase when prompted:
KIALI_PASSPHRASE=$(read -sp 'Kiali Passphrase: ' pval && echo -n $pval | base64)

#- To create a secret, run the following commands:
NAMESPACE=istio-system
kubectl create namespace $NAMESPACE
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: kiali
  namespace: $NAMESPACE
  labels:
    app: kiali
type: Opaque
data:
  username: $KIALI_USERNAME
  passphrase: $KIALI_PASSPHRASE
EOF
