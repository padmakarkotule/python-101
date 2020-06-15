# Jenkins
Ref. [https://www.udemy.com/course/jenkins-beginner-tutorial-step-by-step/learn/lecture/10074974#overview]
**Learn Jenkins from scratch**

About Author of this course,

Raghav Pal
Automation Test Architect | Educator | 10 yrs

    `
        We often need someone to hold our hand and help us take the first few steps before we learn to walk and run.  
        This is the vision behind Automation Step by Step
        
        1. Start from scratch
        2. Break down the topic
        3. Simplify things
        4. Go step by step
        
        Teaching is my passion and I design every course so you can start from scratch, knowing nothing about a topic and become an expert after the course and can work on enterprise projects.
        
        I was an Automation Test Architect for 10 years.
        I experienced that often many topics were made complex than they really are.
    `

Description - **Jenkins is a Automation and CI Tool, it's is a java application.**

## Introduction
## ROLES AND CONFIGURATIONS BASICS 
## JOBS
- How to create basic jobs in Jenkins (Basic job configuration)
- How run job remotely
- How to chain job execution
#### Step1 - How to create basic jobs in Jenkins & Basic job configuration
- Jenkins - New Item - add details
    - Using UI
        - Steps - Jenkins UI -> New Item -> add detail
            - There 5 sections are available,
                - General (Project name, description etc.. )
                - Source Code Management(SCM) 
                    - Add details of SCM such as git, bitbucket etc.
                - Build Triggers - Different options are available E.g.
                    - Trigger builds remotely
                        Need token from system to authenticate. E.g.
                        curl -X POST "https://username:api-token@JENKINS_URL/job/Example/build"
                    - Build after other projects are build
                        It will wait to complete dependent projects and then it will execute it.
                    - Build Periodically 
                        Build should trigger as per schedule similar to crontab
                    - Poll SCM 
                        Poll SCM means as soon as build merge in branch then build 
                        should trigger           
                - Build
                    - In build phase add the basic steps how build should execute e.g.
                        - Execute shell
                        - Execute windows batch command
                        - Invoke top level Maven Target
                        - Plugin or - install plugin and execute e.g. Ansible plugin
                - Post Build Actions
                    - Post Actions are important, this will give option what exactly
                        what are the steps you would like to execute after execution 
                        of build. E.g.
                        - Archive the artificates 
                        - Aggregate the downstream result.
                        - Build other projects
                        - Publish Junit test result report
                        - Publish performance test result report
                        - Record fingerprints of files to track usage
#### Step2 - How to trigger job remotely
        - Steps - How to trigger job remotely
            You can execute build from remotely. E.g.
            - Click on Build Triggers - Build Triggers remotely
            - Enter authentication token (e.g. 123, or pass123), it's consider as password.
            - Goto browser, enter Jenkins IP and port and give job name and enter e.g.
                e.g. http://localhost:8080/job/Test1/build?token=1234
                Note - Test1 is job name
                
#### Step3 - How to chanin job execution
Create 3-4 Porjects to check scenario. It covers dependency of Projects.       
        - Step1 - Build Triggers
            - Go to configuration of any project e.g. Test2
            - Click on Build Triggers
            - Click on build after other projects are build 
                e.g. Istio installation should run after Kubernetes installation else you
                should see some failers.
            - Specify Project names
                E.g. Test1, Test3 
                    This means Test2 project should build after Test1, Test3
                 Options (Also select the options such as)
                 - Triggers only build is stable
                 - Triggers even build is unstable
                 - Trigger even build is failure         
        - Step2 Post Build Actions
            - Build other projects
                - Projects to build (e.g. Test2)
## Integration with GIT

## PIPELINES | DEPLOYMENTS | INTEGRATION
Deployment Pipeline. Below are the stages of deployment(Build, deploy, test and Release).
and corresponding of every stage there will be corresponding jobs.

  **Build -> Deploy -> Test -> Release** (CI Pipe line)
 -> Job   -> Job    -> Job  -> job      (Corresponding jobs)
 -> Notification -> Notifi. -> Notifi. -> Notifi (Every jobs notification whether success of fail of jobs)

and all these jobs are chained. Chained means only success of each build it will
proceed of next stage.

#### CI - Continures Integration Pipe Line
Continues Integration Steps,
1. GIT - Develop & Commit  - Developer develop of fix code and do Commit the changes with git 
    or any version controls systems.
2. Build - Checkout and build the job
    - By executing peridocially 
    - Or by POLL mechanisms
        Out come build process is project artificates e.g. .war file or .exe file
        Move artificate to artificate repo server. e.g. Nexcuss or Jfrog
3. Deploy - build the the war or ear, or .exe or other build file and deploy it on Test environment.
        It may be having multiple Test environment such as 
        - Functions Test environment
        - Performance Test envrionment
4. Test - Execute the automated test scripts e.g. Selinum build
5. Release for Continuous Delivery 
    

#### CD - Continues Deployment Pipe Line
Deploy on Staging env.
Deploy on Production env.
Methods - Blue Green deployments, Canary deployments


#### Install different Plugins
Install different Plugins (Jenkins -> Manage Jenkins - > Plugins)
e.g.
    - Deploy Plugin
    - Kubernetes Plugin (and confgiure credentials)
    - Ansible
 
## CI/CD Steps
1. Configure Jenkins
2. Install Plugins as per deployment and environment needed.
3. Create Build Jobs in Jenkins 
    - General (Project name, description etc.. )
    - Source Code Management(SCM) git
    - Build Trigger (Trigger build from remotely, POLL SCM, Run Periodically etc)
    - Build (Create artificates or docker image)
    - Post build actions (e.g. execute other project)
4. Add Post build actions
    - Deploy War/ear artificates in Docker to build image with versions
5. Configure application specific settings 
    e.g. In tomcat user.xml file add user for deployment
6. Run and Validate
        
## Tips & Tricks
# Email
- **Email** configuration or **Email-ext plugin**
    - Manage settings - Email - SMTP configuration
- **Send in JSON format**
- **Webhook** Send on any REST Call use **Extrame Notification Plugins**

# Pipelines
Pipeline is workflow with group of events and jobs that are chained and integrated 
with each other in sequence.
Every job in pipeline has some dependency one or more other jobs.

# Setup Build Pipeline (CI)

    - Install Build pipeline Plugin
    - Build docker images
    - Packaging using HELM
        - Helm charts
            A package to create version and publish application
            Typically it consist of,
            - Chart.yaml
            - values.yaml
            - templates folder
        - Helm Release
            - An instance of deployed charts
        - Helm Repository
            -         
    - Install app, update, rollback using Helm
    - Monitor application

# Setup Delivery pipeline (CD)

    - Install Delivery pipeline plugin

## Jenkins on Tomcat






