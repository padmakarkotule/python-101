
# Include statment
Ref. url - https://docs.ansible.com/ansible/2.3/playbooks_roles.html.

While it is possible to write a playbook in one very large file 
(and you might start out learning playbooks this way), eventually 
you’ll want to reuse files and start to organize things.

**Roles:**
Q. What is the best way to organize your playbooks? 
The short answer is to use roles! Roles are ways of automatically loading 
certain vars_files, tasks, and handlers based on a known file structure. 
Roles in Ansible build on the idea of include files and combine them to 
form clean, reusable abstractions – they allow you to focus more on the 
big picture and only dive down into the details when needed. 
*Roles are just automation around ‘include’ directives.*
Example project structure:

    root(ansible home folder)
        | -- inventory_hosts.development_env    
        | -- inventory_hosts.staging_env
        | -- inventory_hosts.production_env
        | -- ansible.cfg
        | -- extra_var.json
        | -- Pattern1_IaaS_RHEL7.x.yml
        | -- Pattern2_PaaS_RHEL7.x.yml
    
        group_vars
        | -- all.yml
        
        logs
        | --ansible.log
            
        roles/common
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
        roles/httpd
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
*In a playbook (Pattern - IaaS or PaaS pattern, E.g. Pattern1_IaaS_RHEL7.x.yml)*

**To simplify prereq, install, post task (cleanup and gather_evidance), 
   use pre_tasks and post_tasks.**

**Note: pre_task will execute before any role and post_task will execute after role.** 
            
   
    ---
    - hosts: linuxhost
   
      pre_tasks:
        - name: Executing common and prereq tasks
          # include: "roles/common/tasks/common_task.yml"
          # This is example of include complete role
          include_role:
            name: common
          tags: "prereq"
    
      roles:
        - httpd
    
      post_tasks:
        # This is example of to include particular task. Note in particular task you must include varible file e.g. vars/main.yml file.
        - name: Executing post task.
          include: "roles/common/tasks/cleanup.yml"
          tags: "post_cleanup"
    ansible@bec5c7bc713f:~/ansible$

    **Or Simple add 2 roles**
    ---
    - hosts: webservers
      roles:
         - common
         - httpd


  
**Role Dependencies**
Role dependencies allow you to automatically pull in other roles when using a role. 
**Role dependencies are stored in the meta/main.yml file contained within the role directory.* 
This file should contain a list of roles and parameters to insert before 
the specified role, such as the following in an example roles/myapp/meta/main.yml
Example,

    ---
    dependencies:
      - { role: common, some_parameter: 3 }
      - { role: apache, apache_port: 80 }
      - { role: postgres, dbname: blarg, other_parameter: 12 }

Role dependencies can also be specified as a full path, just like top level roles:

    ---
    dependencies:
    - { role: '/path/to/common/roles/foo', x: 1 }
   
**include_vars**
The include_vars module can be used in a playbook or role to load variables 
from a file. Simply set the value of include_vars to a local file to load 
the variables it contains:
    
    ---
    # ./hello_world.yml
    
    - name: print greeting
      hosts: "*"
      tasks:
        - include_vars: name_vars.yml
    
        - debug: msg="Hello, {{ name }}!"

**Be careful: any variables you set with set_fact will 
not be overwritten with include_vars**

    ---
    # ./hello_world.yml
    - name: print greeting
      hosts: "*"
      tasks:
        - set_fact: name=Percy
    
        - include_vars: name_vars.yml
    
        - debug: msg="Hello, {{ name }}!"
    
    Despite having include_vars after set_fact, the output will look like this:
    
        ok: [123.123.123.123] => {
         "msg": "Hello, Percy!"
        }
    

*How to include variables from an Ansible vault file*

Including variables from an Ansible Vault file 
works the same way as including a regular plaintext vars file.

    ---
    # ./configure_app_servers.yml

    - name: configure app servers
      hosts: app_servers
      pre_tasks:
        - name: include env vars
          include_vars: "{{ env }}.yml"
          tags: ["always"]
    
        - name: include vault for env
          include_vars: "{{ env }}.vault.yml"
          tags: ["always"]
      roles:
        ...

*How to include variables for each item in a loop*

    ---
    # ./configure_app_servers.yml
    - name: configure app servers
      hosts: app_servers
      pre_tasks:
        - name: include vars and vault for env
          include_vars: "{{ item }}.yml"
          tags: ["always"]
          loop:
            - "{{ env }}"
            - "{{ env }}.vault"
      roles:
        ...

*How to include variables using vars_files on a play*

    ---
    # ./configure_app_servers.yml
    
    - name: configure app servers
      hosts: app_servers
      vars_files:
        - "./vars/{{ env }}.yml"
        - "./vars/{{ env }}.vault.yml"
      roles:
        ...

**Task versus Play includes:**
Tasks and plays both use the include keyword, but implement the keyword 
differently. The difference between them is determined by their 
positioning and content. If the include is inside a play it can only 
be a ‘task’ include and include a list of tasks; if it is at the top 
level, it can only include plays. 

Example:

    # this is a 'play' include
    - include: listofplays
    
    - name: another play
      hosts: all
      tasks:
        - debug: msg=hello
    
        "# this is a 'task' include
        - include: stuff.yml
     Another example,    
     tasks:
      - include: tasks/foo.yml

*A ‘task’ include can appear anywhere a task can, but a ‘play’ include 
cannot be inside other play*
    
At a basic level, including task files allows you to break up bits of configuration policy into smaller files. Task includes pull in tasks from other files. Since handlers are tasks too, you can also include handler files from the ‘handler’ section.
By default, starting in Ansible 2.1, ‘task’ includes are automatically 
treated as static rather than dynamic when the include meets the following conditions:
    The include does not use any loops
    The included file name does not use any variables
    The static option is not explicitly disabled (static: no is not present)
    The ansible.cfg options to force static includes (see below) are disabled

