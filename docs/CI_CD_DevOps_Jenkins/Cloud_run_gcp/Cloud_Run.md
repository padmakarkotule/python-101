# Developing Python Code on Cloud Run
**Using Python in Google Cloud with Cloud Run**

How to run a Python app on Google Cloud using Cloud Run.

**Prerequisites**
These labs are based on intermediate knowledge of Google Cloud. 
Whilst we try to cover the steps required in the content, 
it would be helpful to have familiarity with any of the following products:

- Cloud Build
- Cloud Functions
- Cloud Run

###### Login to Google console and open Cloud shell
Open Google Console and run following commands

    # gcloud auth list
    # gcloud config list project
    
###### Create a small application to run on Cloud Run over HTTP

Create simple "Hello word" applition using python flask or Django.

###### Example form Qwicklab
[Qwicklab](https://www.qwiklabs.com/focuses/12677?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=6083462)

**Developing the milli-to-in application code**

Access Abby's code by using Cloud Shell and following the instructions below:
- Clone the following repo <!--> should repo be yours? We can put it elsewhere, right?</!-->


    git clone https://github.com/rosera/serverlesstoolbox.git
- Change the directory to the relevant language directory


    cd ~/serverlesstoolbox/cloud-run/cloud-run-python
    The application separates the user interface from the code making it easy to maintain. 
    Now we have code available, we need to prepare it to be used with Cloud Run.

**Building a Dockerfile and Cloud Build configuration**

- Cloud Run applications are based on Linux containers that use a Dockerfile to 
    define the image manifest.
- View the Dockerfile <!-->please use markdown for codeblocks, do not specify language, 
    this should be 3 blocks, right?</!-->    
    
    
    FROM python:3.8-slim
    COPY . ./
    RUN pip install Flask gunicorn
    CMD gunicorn --bind :$PORT app:app
    
- Google Cloud provides additional tooling to automate the build process for images. 
    Cloud Build is a flexible build automation tool. It can be used with a variety of 
    language runtimes and has a very healthy community of extensions.    

- In this lab, we will use Cloud Build to create our image and upload it to the Container Registry.
    
- Create a file named cloudbuild.yaml:
 
    
    steps:
    - name: gcr.io/cloud-builders/docker
      args: ['build', '-t', 'gcr.io/$PROJECT_ID/milli-to-in', '.']
    - name: 'gcr.io/cloud-builders/docker'
      args: ['push', 'gcr.io/$PROJECT_ID/milli-to-in']    
      
- The file uses Cloud Build to automate build steps. In the above Cloud Build example, 
    the file will perform the following tasks:     
    - Build the Docker image
    - Push the created image to the Cloud Registry     

- Run the automated build process:

    
    gcloud builds submit --config cloudbuild.yaml

**Testing the application**
- starts her investigation by checking the Cloud Run console and 
   sees the **application has not been deployed**.    
   
   It looks like that should be an easy fix from Cloud Shell.          
- Set the Cloud Run region:
    
    
    gcloud config set run/region us-central1
- Deploy the milli-to-in service:


    gcloud beta run deploy milli-to-in \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/milli-to-in \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated   

- Assign the service URL to an environment variable:
   
   
    MILLI_TO_IN_SERVICE=$(gcloud run services list 
    --platform managed --format='value(URL)' --filter="milli-to- in")
- Print the Application Cloud Run URL (keep the result, you can browse to it):


    echo $MILLI_TO_IN_SERVICE
- Select the Cloud Run service just deployed, from the cloud console

- Browse to the URL created for the Cloud Run application. You should see this:

- Enter the value "100" into the application input box then click 
  Convert to validate it is working as expected.    

Over this course of this lab, you have seen how to build a Cloud Run application 
using Google Cloud infrastructure.
    - Write code to solve an issue
    - Deploy code using Cloud Build
    - Resolve an issue using Logging and Trace
    - Redeploy updated code

Next Steps / Learn More
Follow the Serverless Toolbox video series to learn more about how to utilise 
serverless products within your project.
    - Cloud Run
    - Container Registry
    - Cloud Build   
                      