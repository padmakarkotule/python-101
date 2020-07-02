# Cloud Build and Container Registr on Google Cloud Platform

###### Container Registry.
Container Registry provides secure, private Docker image storage on Google Cloud Platform.

###### Cloud build
[Google Cloud build](https://cloud.google.com/cloud-build/docs)

Cloud Build lets you build software quickly across all languages. Get complete control 
over defining custom workflows for building, testing, and deploying across multiple 
environments such as VMs, serverless, Kubernetes, or Firebase.

**Overview**
Continuously build, test, and deploy.
Cloud Build is a service that executes your builds on Google Cloud Platform infrastructure. 
Cloud Build can import source code from Google Cloud Storage, Cloud Source Repositories, 
**GitHub**, or **Bitbucket**, execute a build to your specifications, and 
produce artifacts such as Docker containers or Java archives.

Cloud Build executes your build as a series of build steps, where each build step is run in a 
Docker container. A build step can do anything that can be done from a container 
irrespective of the environment. To perform your tasks, you can either use the supported 
build steps provided by Cloud Build or write your own build steps.

[Quick Start](https://cloud.google.com/cloud-build/docs/quickstarts)
[Git-Hub GoogleCloudBuild/code-examples](https://github.com/GoogleCloudBuild/code-examples)
In above link, check for **quick-start build and quick-start deploy**

## Quickstart: Build

**Preparing source files**

- Assuming already logged in to Google console and opened cloud shell
- Preparing source files
    - Open a terminal window. 
    - Create a new directory named quickstart-docker and navigate into it:
 
    
        mkdir quickstart-docker
        cd quickstart-docker

- Create a file named quickstart.sh with the following contents:


    #!/bin/sh
    echo "Hello, world! The time is $(date)."

- Create a file named Dockerfile with the following contents:

    
    FROM alpine
    COPY quickstart.sh /
    CMD ["/quickstart.sh"]
- Run the following command to make quickstart.sh executable:


    chmod +x quickstart.sh

**Build using Dockerfile**

Cloud Build allows you to build a Docker image using a Dockerfile. You don't require a separate 
Cloud Build config file.

To build using a Dockerfile:

- Get your Cloud project ID by running the following command:


    gcloud config get-value project
- Run the following command from the directory containing quickstart.sh 
  and Dockerfile, where project-id is your Cloud project ID:    
  
    
    gcloud builds submit --tag gcr.io/project-id/quickstart-image
- After the build is complete, you will see an output similar to the following:

    
    DONE
    ----------------------------------------------------------------------------------
    ID              CREATE_TIME                DURATION SOURCE     STATUS
    $BUILD_ID   2016-09-28T13:46:29+00:00  9S    gs://[PROJECT_ID]_cloudbuild/source/1508159187.8-b0d8841d51674a30aebd1e55bb99486f.gz  gcr.io/[PROJECT_ID]/quickstart-image (+1 more)       SUCCESS            

**Build using a build config file**
In this section you will use a Cloud Build config file to build the same 
Docker image as above. The build config file instructs Cloud Build to perform tasks based 
on your specifications.

- **In the same directory that contains quickstart.sh and the Dockerfile**, 
  create a file named **cloudbuild.yaml** with the following contents. 
  This file is your build config file. At build time, Cloud Build automatically 
  replaces $PROJECT_ID with your project ID.
  Sample on git-hub,
  https://github.com/GoogleCloudBuild/code-examples/blob/master/quickstart-build/cloudbuild.yaml

    
    steps:
    - name: 'gcr.io/cloud-builders/docker'
    args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
    images:
    - 'gcr.io/$PROJECT_ID/quickstart-image'
    
- Start the build by running the following command:


    gcloud builds submit --config cloudbuild.yaml
- When the build is complete, you will see an output similar to the following:

    
    DONE
    -------------------------------------------------------------------------------------------------------------------------
    ID                                    CREATE_TIME                DURATION SOURCE                                   STATUS
    $BUILD_ID                             2016-09-28T13:46:29+00:00  8S    gs://[PROJECT_ID]_cloudbuild/source/1508158566.55-725755714baa4b7e9e99984c422ec4e2.gz  gcr.io/[PROJECT-ID]/quickstart-image (+1 more)       SUCCESS    


You've just built quickstart-image using the build config file and pushed the image **to Container Registry.**

**View the build details**
- Open the Cloud Build page in the Google Cloud Console.

- Select your project and click Open.
    You will see the Build history page:

- Click on a particular build.
    You will see the Build details page.
- To view the artifacts of your build, under Build Summary, click Build Artifacts.
    You will see an output similar to the following:
    (Ref. link - https://cloud.google.com/cloud-build/docs/quickstart-build)

**Clean up**
To **avoid incurring charges** to your Google Cloud account for the resources used in this quickstart, 
follow these steps.

- Open the Container Registry page in the Google Cloud Console.
- Select your project and click Open.
- Click quickstart-image.
- Select all the images and click Delete.
You have now deleted the images that you created as part of this quickstart.

 
## Quickstart: Deploy
This page shows you how to use Cloud Build to **deploy a containerized application to Cloud Run.**

[Quick start deploy Ref. link](https://cloud.google.com/cloud-build/docs/quickstart-deploy)

**Before you begin**
- In the Cloud Console, on the project selector page, select or create a Cloud project.
- Make sure that billing is enabled for your Google Cloud project. 
- Enable the Cloud Build and Cloud Run APIs.
- Install and initialize the Cloud SDK.
    **Note** - If you've already installed Cloud SDK previously, make sure you 
    have the latest available version by running 
    **gcloud components update.**

**Grant permissions**
Cloud Build requires **Cloud Run Admin and IAM Service Account User permissions** 
before it can deploy an image to Cloud Run.

- Open a terminal window.
- Set environment variables to store your project ID and project number:

    
    PROJECT_ID=$(gcloud config list --format='value(core.project)')
    PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
- Grant the Cloud Run Admin role to the Cloud Build service account:

    
    gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
    --role=roles/run.admin
- Grant the IAM Service Account User role to the Cloud Build service account 
  for the Cloud Run runtime service account:        



    gcloud iam service-accounts add-iam-policy-binding \
    $PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
    --role=roles/iam.serviceAccountUser

**Deploy a prebuilt image**

**You can configure Cloud Build to deploy a prebuilt image that is stored 
in Container Registry to Cloud Run.**

To deploy a prebuilt image:

- Open a terminal window (if not already open).
- Create a new directory named helloworld and navigate into it:


    mkdir helloworld
    cd helloworld    
- Create a file named **cloudbuild.yaml** with the following contents. **This file is the 
  Cloud Build config file.** It **contains instructions for Cloud Build** to deploy the 
  image named gcr.io/gcbdocs/hello **on the Cloud Run service named cloudrunservice**.
  
  [On git-hub](https://github.com/GoogleCloudBuild/code-examples/blob/master/quickstart-deploy/cloudbuild.yaml) 
  
  
    steps:
    - name: 'gcr.io/cloud-builders/gcloud'
      args:
      - 'run'
      - 'deploy'
      - 'cloudrunservice'
      - '--image'
      - 'gcr.io/gcbdocs/hello'
      - '--region'
      - 'us-central1'
      - '--platform'
      - 'managed'
      - '--allow-unauthenticated'      

- Deploy the image by running the following command:   


    gcloud builds submit --config cloudbuild.yaml

When the build is complete, you will see an output similar to the following:


    DONE
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                                            IMAGES  STATUS
    784653b2-f00e-4c4b-9f5f-96a5f115bef4  2020-01-23T14:53:13+00:00  23S       gs://cloudrunqs-project_cloudbuild/source/1579791193.217726-ea20e1c787fb4784b19fb1273d032df2.tgz  -       SUCCESS       

- You've just deployed the image hello to Cloud Run.


**Run the deployed image**

- Open the Cloud Run page in the Cloud Console:

- Select your project and click Open.
    You will see the Cloud Run Services page.

- In the table, locate the row with the name cloudrunservice, and click cloudrunservice
        The Service details page for cloudrunservice is displayed.

- To run the image that you deployed on cloudrunservice, click the URL:
        