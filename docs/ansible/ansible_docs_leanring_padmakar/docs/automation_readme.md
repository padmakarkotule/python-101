![alt text][logo]
[logo]:/img/logo.jpg
# GS Lab - IDM Cloud Automation
GSLab IDM Cloud Automation Services provide an orchestration and automation platform
with enterprise-ready IaaS and PaaS services to provision VM and 
installation of tools/components. 

Tools - Ansible automation tool considered for this document. 
  
For full documentation of ansible please visit ansible site- 
[Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)

**Note:** In this document, contact, license and other information has given as sample values."
          Actual values will be updated as per requirement/environment.
                 
  
#### Version - 0.1
  
[TermsOfService:](http://gslab.com/terms)

#### Contact:

**IDM Clould automation team** - [Website]("http://gslab.com/contact") [Email](mailto:componentowner@gslab.com)
 

#### License:
> 
      name: "license information"
      url: "https://< https://www.gslab.com/license_info"

#### Servers:
| url        | Description   | 
| ---------- |:-------------:|
http://ansible:5001/ | Ansible Controller Server
http://vCenter:5002/ | vCenter servers (End point) / Public Cloud (E.g. AWS, Google Cloud)   

#### Security:
| url        | Description   | 
| ---------- |:-------------:|
http://ansible:5001/ | Ansible Vault Server (End point)
http://hashicorp vault:5002/ | Hashicorp vault Server (End point) 


#### Tags / Category:
**Info** For each role we will define tag. Following are the 
few examples of tags.

| Name        | Description   | 
| ---------- |:-------------:|
Monitoring tools | (E.g. Nagios)
Backup Tool |  
Directory tools | (E.g. AD, LDAP),
Discovery Mgmt. |  
IP Management | (E.g. Info block), 
Patch Mgmt. | 
Service management | (E.g. SNOW),
Anti-virus | (E.g. Macfee, Trendmicro, etc),
Security | (E.g. Ansible Vault, Vault by HashiCrop, etc),
Disaster Recovery Management | 
Backup | 
Reporting tools |  
Databases |(e.g. MySql, Oracle, Postgre )

#### Domain specific parameters:
All variables are declared in --extra-var.json which will be 
configurable as per domain specific requirements. 
This will also depend upon customer environment.<br>
Example,<br>
The default page size of 16KB is appropriate for a wide range of workloads, 
particularly for queries involving table scans and other operations involving 
bulk updates. Smaller page sizes might be more efficient for OLTP workloads 
involving many small writes, where contention can be an issue when a single 
page contains many rows. Smaller pages might also be efficient with SSD 
storage devices, which typically use small block sizes. Keeping the InnoDB 
page size close to the storage device block size minimizes the amount of 
unchanged data that is rewritten to disk. 
*During roles development, we will update this table.*
                                    Domain specific config value

| Tool Name  | Config paramater  | Telecom | Banking | Healthcare/Insurance |IT Infrastcructure - Service Provider |
| ---------- |:-------------    :|        :|        :|                     :|                                    :|   
|Mysql | Page size E.g. 64KB      | 64k |16k|32k|64k
|      | Buffer Pool E.g. 128M | 128M| | |

#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https://component-docs/ | E.g. https://dev.mysql.com/doc/

Following are the few list of opensource components which customer uses frequently. 
We will add more in list during development as per requirements.
          
## Components (Open Source )- Table of contents
1. [Httpd](#Role - Httpd)
2. [MySql](#Role - MySql)
3. [Messanging Queue](#Role - Messaging Queue - rabbitmq)
4. [File System](#Role - File System)
5. [SSH Implementation](#Role - SSH implementation)
6. [SELinux](#Role - SELinux)
7. [Filebeat](#Role - Filebeat)
8. [Logstash](#Role - logstash)
9. [SNOW](#Role - SNOW)
10. [Jboss](#Role - Jboss)
11. [Tar](#Role - tar)
12. [Unarchive](#Role - unarchive)
13. [Zip](#Role - zip) <br>
Other <br>
14. [System verification, E.g. CPU, RAM validation](#Role - System verification (E.g. RAM/CPU))

## WorkFlow Components - Table of contents
1. [Infoblox IPAM] (#IPAM1)
2. [SolarWinds (IPAM)](#IPAM2)

# Role - Httpd<a name="Role - Httpd"></a>
**Role - httpd role.**
The roles variable, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        gather_evidance
        | --gather_evidance.log
            
        **roles/httpd/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 2.4.41
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: Web server
        description: Web server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://httpd.apache.org/
      
### Paths and Variables 
<dl> 
    <dt> roles/httpd/defaults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```httpd_listen_port: 80``` <br>
            schema:<br>
            ```type: int```<br>
            version: <br>
            ```version: "2.4.41"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/httpd/vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook httpd.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>install_dir":"/opt/httpd_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            Httpd Install dir E.g.:<br>
            ```httpd_install_dir: "/opt/httpd"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

### Files and Templates 
<dl> 
    <dt> roles/httpd/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create a file named index.html containing some sample text. 
              Example,<br>
              ```$cat >index.html```<br>
                ```Hello Word!```<br>
              ```$ cat index.html```<br>
                ```Hello Word!```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of our httpd.conf file **by copying an existing 
              one from a fresh install of httpd.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/httpd<br>
                httpd_listen_port: 80<br>
                httpd_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat >httpd.conf.j2```<br>
                   listen "{{ httpd_listen_port }}"<br>
                   loglevel "{{ httpd_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

### Handlers 
<dl> 
    <dt> roles/httpd/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart HTTPd 
            ***in "roles/httpd/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart HTTPd```<br> 
                ```service:```<br> 
                ```name: httpd``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart HTTPd```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart HTTPd"```<br>
             </p>
        </dd>
</dl>

### Tasks 
<dl> 
    <dt> roles/httpd/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install Httpd
              yum: name=httpd state=latest  
        </dd>
</dl>

### README.md

###### Role name: httpd <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

### META
        |-- meta
        |   `-- main.yml

<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: httpd playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - MySql <a name="Role - MySql"></a>

**Role - Mysql role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - <component verersion>
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

### Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

### Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

### Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

### README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
</p>

#Role - Messaging Queue (rabbitmq) <a name="Role - Messaging Queue - rabbitmq"></a>
**Role - Messaging Queue role.** <br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - <component verersion
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: < Comp > <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
</p>

# Role - File System<a name="Role - File System"></a>

**Role - File System role.**
**Note** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - SSH implementation<a name="Role - SSH implementation"></a>

**Role - SSH role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - SELinux<a name="Role - SELinux"></a>

**Role - SELinux role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Filebeat<a name="Role - Filebeat"></a>

**Role - Filebeat role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Logstash<a name="Role - logstash"></a>

**Role - Logstash role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - SNOW<a name="Role - SNOW"></a>

**Role - SNOW role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Jboss<a name="Role - Jboss"></a>

**Role - Jboss role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Tar<a name="Role - tar"></a>

**Role - Tar role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Unarchive<a name="Role - unarchive"></a>

**Role - Unarchive role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Zip<a name="Role - zip"></a>

**Role - Zip role.**<br>
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# Role - Comman (Which includes system verification E.g. RAM/CPU)<a name="Role - System verification (E.g. RAM/CPU)"></a>

**Role - Common role.**
**Note -** Replace <comp> with actual role/component name. 

The roles variables, tasks, files, handlers, etc. ate stored in following directory structure format.  
    
    root(ansible home folder)
        | -- inventory_hosts    
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
        
        | --gather_evidance
            
        **roles/<comp>/**
        |-- README.md
        |-- defaults
        |   -- main.yml     
        |-- files      
        |-- handlers
        |   -- main.yml
        |-- meta
        |   -- main.yml
        |-- tasks
        |   -- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   -- test.yml
        `-- vars
            -- main.yml
  
#### Component Version - 
  
#### Component License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Component Security: 
**Note** Will keep all security related information of particular component in security section.
E.g. under this section Service user password will be stored of
ansible vault or Hashicorp vault or any third part vault system. *(If applicable)*

| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
Or
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)
OR
(Thrid pary vault)

#### Tags:
      - name: <  > server 
        description: < > server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// component-docs/     | Tools/Component Documentation
E.g. https://<comp>.org/
      
## Paths and Variables 
<dl> 
    <dt> roles//<comp>faults/main.yml </dt>
        <dd>
            Summary:<p>
            Default attributes used for this component. </p>
            Description:<p>
            In this file use variables related only of <br> 
            this component and not generic such as repo server, temp dir, etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Variable name and it's value. <br>
            ```<var1>: <Value>``` <br>
            schema:<br>
            ```type: <E.g. int?```<br>
            version: <br>
            ```version: "<Comp. ver>"```<br>
            schema:<br>
            ```type: string```<br>  
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/<comp>vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Note:- For this component, there is no internal variable. All common variables are stored in 
            common role such as temp_dir, log dir etc.
            Following are the few example of internal variables will be stored in common role.
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/binaries/<windows or linux>/<application>/<version>/"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/<applicaton installion path>"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "/var/log/gsl/<application>/<app_name>.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "appname_<version>.ext"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "/tmp/gsl/artifacts/<application_name>/installers"```<br>
            Schema:<br>
            ```type: string```<br>        
            </p>
        </dd>
</dl>  
<dl> 
    <dt> group_vars/all.yml </dt>
        <dd>
            Summary:<p>
            Variables listed here are applicable to all host groups. </p>
            Description:<p>
            In this file use variables which are applicable to all host groups.
            E.g. ntp server, dnsserver etc.</p>
        </dd>
        **Variables:**
        <dd>
            <p>
            NTP Server:<br>
            ```ntpserver: 192.168.1.2``` <br>
            Schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           
<dl> 
    <dt> extra_vars.json </dt>
        <dd>
            Summary:<p>
            Passing variables on the command line. </p>
            Description:<p>
            In addition to vars_prompt and vars_files, it is possible to 
            set variables at the command line using the --extra-vars (or -e) argument. 
            Variables can be defined using a single quoted string 
            (containing one or more variables) using one of the formats below.
            Example,
            ansible-playbook <comp>.yml --extra-vars "version=2.4.1 other_variable=foo"
            **Note:** Values passed in using the key=value syntax are interpreted as 
            strings. Use the JSON format if you need to pass in anything that shouldn’t 
            be a string (Booleans, integers, floats, lists etc).
            Using json/yml format
            ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
            ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
            **vars from a JSON or YAML file:**
            ansible-playbook release.yml --extra-vars "@extra_var.json"
            E.g. of extra_var.json
            {
                "ansible_sudo_pass":ansible123,
                "<comp>_install_dir":"/opt/<comp<_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: " ",``` <br>
            Schema:<br>
            ```type: string```<br>
            <comp> Install dir E.g.:<br>
            ```<comp>_install_dir: "/opt/<comp>"``` <br>
            Schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>

## Files and Templates 
<dl> 
    <dt> roles/<comp>/templates </dt>
        <dd>
            Summary:<p>
            To copy files use with the copy resource and for script files use script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a destination location.
            If you need variable interpolation in copied files, use the template 
            module. Using a variable in the content field will result in unpredictable output.
            For Windows targets, use the win_copy module instead.<br>
            ***Ansible does not need a path for resources stored in them when working in the role. 
            Ansible checks them first. You may still use the full path if you want to reference 
            files outside of the role, however, best practices suggest that you keep all of 
            the role components together.***<br>
            </p>
        </dd>
        **files:**
        <dd>
            <p>
              Create/keep component specific files here. 
              Example,<br>
              ```$cat >config.ini```<br>
            </p>
        </dd>
        **templates:**
        <dd>
            <p>
              create a template of config file **by copying an existing 
              one from a fresh install of it.**<br> 
              Define a couple of default variables in our role and replace it in
              template using variable name. E.g.
              E.g. We will do a default listening port of 80 and a LogLevel that 
              will default to warn. We can do this by adding an entry to defaults/main.yml:
              Example,<br>
              ```$cat defaults/main.yml```<br>
              ---<br>
              # defaults file for roles/<comp><br>
                <comp>_listen_port: 80<br>
                <comp>_log_level: war<br>
              **Create template file, E.g.:**<br>
              ```$ cd templates```<br>
              ```$ cat ><comp>.conf.j2```<br>
                   listen "{{ <comp>_listen_port }}"<br>
                   loglevel "{{ <comp>_log_level }}"<br>  
              **Note:** template file has the .j2 extension. <br>
            </p>
        </dd>
</dl>

## Handlers 
<dl> 
    <dt> roles/<comp>/handlers  </dt>
        <dd>
            <p>
            Summary: Contains handlers, which may be used by this role or even anywhere outside this role </p>
            Description: <p>
            Ansible handlers are simply tasks that may be flagged during a 
            play to run at the play’s completion.</p>
            Example:<p>
            Create the handler for the Restart <Comp> 
            ***in "roles/<comp>/handlers/main.yml"***
            with the following content,<br>
            ```---```<br>
            ```- name: Restart <Comp>```<br> 
                ```service:```<br> 
                ```name: <comp>``` <br>
                ```state: restarted``` <br> 
                ```become: True``` <br>
            and in task, you can specify notify e.g. <br>
            tasks:<br>
            ```---```<br>
            ```- name: Restart <comp>```<br>
                 ```command: echo "this task will restart the web services"```<br>
                 ```notify: "Restart <comp>"```<br>
             </p>
        </dd>
</dl>

## Tasks 
<dl> 
    <dt> roles/<comp>/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>
            E.g.
            - name: Install <Comp>
              yum: name=<comp> state=latest  
        </dd>
</dl>

## README.md

###### Role name: <Comp> <br>
Instructions for use of the component.

###### Running the playbook:
Usage - Example

###### Gather evidance
Provide gather evidance location e.g. gather_evidance/gather_evidance.log

######Clean up<br>
- Delete any empty/unused boilerplate folders and YAML files.<br>
- rename readme.md to README.md (Ansible Galaxy requires the filename to be uppercase.)

## META
        |-- meta
        |   `-- main.yml
<p>
    Summary:<p> 
        When Galaxy imports a role, the import process looks for 
        metadata found in the role’s meta/main.yml file. </p>  
    Description:<p>
        Role dependencies allow you to automatically pull in other roles 
        when using a role. Role dependencies are stored in the meta/main.yml 
        file contained within the role directory. </p>
    Update meta/main.yml file:<br>
    Example,<br>
    <p> 
    galaxy_info:
        author: GSL Team<br>
        description: <comp> playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

# WorkFlow Components
<VMware deployment Example>

## Example of VM deploy
Example <>

## Example of workflow with other tools

#### VM hostname generation

#### IPAM1 
IP Addres management tool - Infoblox 


#### IPAM2 
IP Addres management tool - SolarWinds



