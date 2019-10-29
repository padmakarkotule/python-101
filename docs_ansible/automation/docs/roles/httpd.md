![alt text][logo]
[logo]:/img/gslab.jpg
# Role - httpd 
This is ansible httpd role.
The roles variables, tasks, files, and handlers that are stored in following structure.  
        
        roles/httpd/
        
        |-- README.md
        
        |-- defaults
        |   `-- main.yml
        
        |-- files
        
        |-- handlers
        |   `-- main.yml
        |-- meta
        |   `-- main.yml
        |-- tasks
        |   `-- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   `-- test.yml
        `-- vars
            `-- main.yml

**Note:** Sample value provided for contact and license information."
  
#### <component> Version - 2.4.41
  
[TermsOfService:](http://gslab.com/terms)

#### Contact:

**IDM Clould automation team** - [Website]("http://gslab.com/contact") [Email](mailto:componentowner@gslab.com)
 

#### License:
> 
      name: "Component license information"
      url: "https://<component - license >/license_info"

#### Servers:
| url        | Description   | 
| ---------- |:-------------:|
http://ansible:5001/ | Ansible Controller Server
http://vCenter:5002/ | vCenter servers (End point) / Public Cloud (E.g. AWS, Google Cloud)   

#### Security:
| url        | Description   | 
| ---------- |:-------------:|
http://ansibleVault:5001/ | Ansible Vault Server (End point)
http://hashicorp vault:5002/ | Hashicorp vault Server (End point)

#### Tags:
      - name: Web server
        description: Web server
        
#### ExternalDocs:
| url        | Description   | 
| ---------- |:-------------:|
https:// <component-docs\>/     | < Tools/Component> Documentation
E.g. https://httpd.apache.org/
      
## Paths and Variables 
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
            </p>
        </dd>
</dl>           
<dl> 
    <dt> roles/httpd/vars/main.yml </dt>
        <dd>
            Summary:<p>
            The variables defined in this directory are meant for role internal use only. </p>
            Description:<p>
            It is a good idea to namespace your role variable names, to prevent potential 
            naming conflicts with variables outside of your role. For example, if you needed 
            a variable named config_file in your baseline playbook, you may want to name your  
            variable baseline_config_file, to avoid conflicts with another possible config_file 
            variable defined elsewhere.
            </p>
        </dd>
        **Variables: (Variable name and it's values)**
        <dd>
            <p>
            Temp dir: <br>
            ```temp_dir: "/tmp/gsl/"``` <br>
            schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/downlods/httpd"```<br>
            schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/opt/httpd"```<br>
            schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "./logs/ansible.log"```<br>
            schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "NA"```<br>
            schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "NA"```<br>
            schema:<br>
            ```type: string```<br>
            version: <br>
            ```version: "2.4.41"```<br>
            schema:<br>
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
            schema:<br>
            ```type: string```<br>
            DNS Server:<br>
            ```dnsserver: 192.168.1.1``` <br>
            schema:<br>
            ```type: string```<br>
            Git repo: <br>
            ```repository: https://github.com/playbooks.git```<br>
            </p>
        </dd>
</dl>           

|-- README.md
        
        |-- 
        |   `-- 
        
        |-- files
        
        |-- handlers
        |   `-- main.yml
        |-- meta
        |   `-- main.yml
        |-- tasks
        |   `-- main.yml
        |-- templates
        |-- tests
        |   |-- inventory
        |   `-- test.yml
        `-- vars
            `-- main.yml