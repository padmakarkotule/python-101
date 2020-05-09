# GCP - Initial Setup and Requirements - As per Qwiklabs

Login to GCP console - https://console.cloud.google.com

## Activate Google Cloud Shell

Google Cloud Shell is a virtual machine that is loaded with development tools. 
It offers a persistent 5GB home directory and runs on the Google Cloud. Google 
Cloud Shell provides command-line access to your Google Cloud resources.

1. In the Google Cloud Console, on the top right toolbar, 
   click the Activate Cloud Shell button.
2. Click Continue
   It takes a few moments to provision and connect to the environment. 
   When you are connected, you are already authenticated, and the 
   project is set to your PROJECT_ID. For example,
   
   `Welcome to Cloud Shell! Type "help" to get started.
    To set your Cloud Platform project in this session use “gcloud config set project [PROJECT_ID]”
    padmakar_kotule@cloudshell:~$`
    
gcloud is the command-line tool for Google Cloud. It comes pre-installed on Cloud Shell and supports tab-completion.
You can list the active account name with this command:

    `padmakar_kotule@cloudshell:~$ gcloud auth list
      Credentialed Accounts
    ACTIVE  ACCOUNT
    *       padmakar.kotule@gmail.com
    To set the active account, run:
        $ gcloud config set account `ACCOUNT`  
    padmakar_kotule@cloudshell:~$`

You can list the project ID with this command:

    `gcloud config list project
    padmakar_kotule@cloudshell:~$ gcloud config list project
    [core]
    project = sample-ui-test-231709
    
    Your active configuration is: [cloudshell-14645]
    padmakar_kotule@cloudshell:~$`
    
## Configuring environment variables E.g. Configure cluster (Kubernetes) access for kubectl

    `
    export GCLOUD_PROJECT=$(gcloud config get-value project)`
    export CLUSTER_NAME=central
    export CLUSTER_ZONE=us-central1-b
    
    `


