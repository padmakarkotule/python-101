# Istio_Overview_and_Architecture

**What is Istio on GKE?**

Istio on GKE is a tool that provides automated installation and upgrade of Istio in your 
GKE cluster. When you upgrade GKE, the add-on is automatically upgraded to the most 
recent GKE-supported version of Istio. This lets you easily manage the installation and 
upgrade of Istio as part of the GKE cluster lifecycle.

It is important to note that, when using Istio on GKE, Istio will be running inside 
your cluster. **There is no service level agreement (SLA)** on the Istio components 
running in your cluster.

# Goolge - Istio on GKE

**Should I use Istio on GKE?**

While Istio on GKE does manage installation and upgrade, it uses default installation 
options for the control plane that are suited for most needs. However, you should 
be aware of these limitations:

    The version of Istio installed is tied to the GKE version, and you will not be able 
    to update them independently. There are strong limitations over the configuration of 
    the control plane. You should review these limitations before using the Istio on 
    GKE add-on in production.

If you need to use a more recent open source version of Istio, or want greater control 
over your Istio control plane configuration (which may happen in some production use 
cases), we recommend that you use the open source version of Istio rather than the Istio 
on GKE add-on.
If you no longer want to use our automatic installation functionality for whatever reason, 
you can uninstall the add-on. You can find out how to do this in 
Uninstalling Istio on GKE. - https://cloud.google.com/istio/docs/istio-on-gke/uninstalling
