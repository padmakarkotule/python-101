# ansible_aws

    
Ansible AWX is an open source web application that provides a user interface, REST API, and task engine for Ansible. It's the open source version of the Ansible Tower. The AWX allows you to manage Ansible playbooks, inventories, and schedule jobs to run using the web interface.

https://github.com/ansible/awx
System Requirements
The system that runs the AWX service will need to satisfy the following requirements
At least 4GB of memory
At least 2 cpu cores
At least 20GB of space
Running Docker, Openshift, or Kubernetes
If you choose to use an external PostgreSQL database, please note that the minimum version is 10+.
OS 
Ubuntu version - Ubuntu_Server_16.04_LTS
CentOS - 
RHEL - 
Software Prerequisites
Before you can run a deployment, you'll need the following installed in your local environment:
Ansible Requires Version 2.8+
Docker
A recent version
docker Python module
This is incompatible with docker-py. If you have previously installed docker-py, please uninstall it.
We use this module instead of docker-py because it is what the docker-compose Python module requires.
GNU Make
Git Requires Version 1.8.4+
Node 10.x LTS version
NPM 6.x LTS
Python 3.6+

Installation:

Note: Awx installation steps on Ubuntu machine
You can also use installation script : 
========================================
https://github.com/RohitMalakarGslab/ansible_aws/blob/master/AWX_installation.sh
=========================================
=============================================================
Open awx UI
==============================================================
http://localhost:8080
username: admin
password: password

Running a playbook on the AWX server
Perform the following steps to run a playbook:
Log in to the AWX server with the default credentials (user name as admin and password as password).
Default username and password after installation of AWX are
Username: admin
password: password
Figure 1. Login Page
On the home page or the dashboard, you can see information about your AWX server and its overall status that includes the following details:
Number of hosts who have successfully run the playbooks
Number of hosts who failed to run the playbooks
Total number of inventories
Number of projects and the sync status
Graph of playbook that has been run throughout
Figure 2. Dashboard

2. Add a new organization.
On the dashboard, click ORGANIZATIONS on the left pane.
Click ADD and enter a name and a brief description for the new organization.
Click SAVE to save changes.
 
 
Figure 3. Creating a new organization


3. Add a new user 
On the left pane, click USERS.
Enter the first name and the last name for the user.
Enter organization you created in the previous step.
Enter a working email ID and a specify the user name and password to log in to the server.
Select the User type as per the access rights to be given. Users can be of any one of the following types:
Normal user – is a member of an organization who can create new templates, use templates, and update templates.
System auditor – is a member of an organization who can view inventory, templates, and job status but cannot create or modify anything on the server.
System administrator – has all the privileges on the server (same as the default root/admin).
Click Save to save changes.
Figure 4. Create a new user

Other authentication mechanism e.g.
Active Directory
Google Authentication
Etc..
 
 
4. Add a new inventory.
Adding an inventory is a task to add hosts to the server. All your remote hosts will come under inventory. An inventory can be divided into groups, such as development, testing, and production servers. To add a new inventory:
On the left pane, click INVENTORIES.
Click ADD INVENTORY.
Enter a name and specify an organization for the inventory.
Click SAVE to save changes.
Generic question - What hostname and IP address need to use to provision new VM (e.g. EC2 on AWS, as we don’t know the IP address unless it’s deployed)
Figure 5. Create a new inventory

5. Add hosts.
Host name can be a working IP address or a URL. For example, 192.168.1.23 or aaa.company.com.
In the same inventory page previously created, click the HOSTS tab.
Then click ADD HOST.
Enter the host name of the machine you need to add.
Enter a description of the machine.
Click SAVE to save changes. You can add any number of hosts to an inventory.
Figure 6. Add a host to inventory

6. Add credentials.
In AWX, credentials are stored separately. This is very efficient in a LDAP scenario where we can use a single credential to any number of hosts.
We will explore more on this part. 
On the left pane, click CREDENTIALS.
Click ADD and enter a name and description for the new credential.
Select an organization for the credential.
Select a credential type (Machine – similar to SSH login).
Enter the username and password of the remote machine.
Click SAVE to save changes made.
Figure 7. Add credentials of corresponding host.

7. Add a new project.
On the left pane, click PROJECTS.
Click ADD.
Enter a name and description for the project.
Select an organization and an SCM type. When you add a new project, the base path to the repository is given. Base path can be the link to your GitHub repository or the directory holding playbooks. If file is present on the AWX server, then select Manual and enter the base path to the file. In our case, we will select Git as our SCM Type because we will be using the GitHub repository. The other SCM types are Manual, Mercurial, Subversion, Red Hat Insights.
Enter SCM URL/Playbook directory. Here, we will add a public GitHub repository: https://github.com/cupofcaffeine/ansible. You can select the required options from the SCM UPDATE OPTIONS section.
Click SAVE to save changes.
Figure 8. Creating a project

 
8. Add a new template.
Here we select the specific playbook to be executed from the project we added.
On the left pane, click TEMPLATES.
Enter a name and description for the template.
Select the job type as Run or Check.
Select the inventory and the project in which your playbooks are present.
Select your playbook from the PLAYBOOK drop-down list.
Add credentials for the particular inventory of hosts.
Select your preference to log type in verbosity. Verbosity refers to the log type you might need while running the playbook.
Click SAVE to save changes.
Figure 9. Creating template

9. Run the required job.
On the TEMPLATES page, select the template you want to run and click the job launcher icon.
Figure 10. Running a job

You will be redirected to the currently running job page. Notice that the verbose of the job you just ran is displayed.
Observe if the job ran successfully or not.
Green indicates that it is successful.
Orange indicates that the commands are executed, and changes are made/edited.
Red indicates warnings or errors.
Figure 11. Verbose to job executed

 
Ansible awx REST API access:
Ansible AWX / Ansible Tower supports RESTfull API calls. It provides greater flexibility that you no need to be in Ansible Tower/AWX console to start the template or read the ansible job results. You could post the API from anywhere. It could be a web portal or from your laptop using POSTMAN/SoapUI. This article will demonstrate how to POST job using API and how to read the job result using the GET method.
1. Here is the template and template ID. If you keep the mouse near to that template, you can see the template id in the bottom of the screen.

2. How to navigate to AWX/ Ansible Tower API? Please refer to the following screenshot.
http://10.43.12.71:8080/api/v2/

 
3. You could access the job template REST API like below.
For Ex.: http://10.43.12.71:8080/api/v2/job_templates/20/

 
4. Launched an template using postman app


LDAP configuration:

Login with admin credentials and configure LDAP

Go to setting →  AUTHENTICATION → Choose LDAP and fill required details for configuration.
https://docs.ansible.com/ansible-tower/latest/html/administration/ldap_auth.html




Project hierarchy:

	







	User 1, User2, User3                                                    User 1, User2, User3

