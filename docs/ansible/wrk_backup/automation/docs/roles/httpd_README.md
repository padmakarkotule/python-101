![alt text][logo]
[logo]:/img/logo.jpg
# Role - httpd 
This is ansible httpd role.
The roles variables, tasks, files, and handlers that are stored in following structure.  
    
    root(ansible home folder)
        | -- inventory_hosts.development    
        | -- inventory_hosts.staging
        | -- inventory_hosts.production
        | -- ansible.cfg
        | -- extra_var.json
        | -- pattern_IaaS.yml
        | -- pattern_PaaS.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
            
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
            Schema:<br>
            ```type: string```<br>
            Software Repo path: <br>
            ```repo_path: "http://reposerver/downlods/httpd"```<br>
            Schema:<br>
            ```type: string```</br>
            Installation directory: <br>
            ```install_dir: "/opt/httpd"```<br>
            Schema:<br>
            ```type: string```<br>
            Log directory: <br>
            ```log_dir: "./logs/ansible.log"```<br>
            Schema:<br>
            ```type: string```<br>
            Archive name: <br>
            ```archive_name: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            Fixpack name: <br>
            ```fix_pack: "NA"```<br>
            Schema:<br>
            ```type: string```<br>
            expand area: <br>
            ```expand_area: "NA"```<br>
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
                "mysql_install_dir":"/opt/httpd_in_exta_var"
            }
            </p>
        </dd>
        **Variables:**
        <dd>
            <p>
            Sudo Password:<br>
            ```ansible_sudo_pass: ansible123,``` <br>
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

## Files and Templates 
<dl> 
    <dt> roles/httpd/templates </dt>
        <dd>
            Summary:<p>
            Fles for use with the copy resource amd script files for use with the script resource. </p>
            Description:<p>
            The copy module copies a file from the local or remote machine to a location 
            on the remote machine.
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

## Handlers 
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

## Tasks 
<dl> 
    <dt> roles/httpd/files </dt>
        <dd>
            <p>
            Summary: Ansible Tasks. </p>
            Descripton:<p> 
            Create Tasks for <tool/component> role as per <tool/component> documentation.</p>  
        </dd>
</dl>

## README.md

###### Role name: httpd <br>
Instructions for use:

###### Running the playbook:
Usage - 

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
        description: httpd playbook
        company: GS Lab <br>
        license: license (GPL-2.0-or-later, MIT, etc)<br>
        min_ansible_version: 2.4 <br>
        galaxy_tags: []<br>
        dependencies: []<br>   
    </p>

