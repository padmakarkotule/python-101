#!/bin/bash

#Installation:
sudo apt-get update
sudo apt update && sudo apt install python -y

echo "Install Ansible"
echo "============================================================"
sudo apt-get install -y software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt-get install -y ansible
sleep 1

echo "Install docker"
echo "============================================================"
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update && sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sleep 3

echo "Install Python-pip, Docker-compose"
echo "============================================================"
sudo apt install git python-pip -y
sudo pip install docker-compose==1.9.0
sleep 3
echo "Install NodeJS, NPM"
echo "============================================================"
sudo apt install nodejs npm -y
sudo npm install npm --global
sleep 1
echo "Install Git & Clone Repository AWX"
echo "============================================================"
sudo apt install git
cd /root
git clone https://github.com/ansible/awx.git
cd awx/installer/


echo "Generate Secret Key & Edit Inventory File"
echo "============================================================"
sudo secret_key=`openssl rand -hex 32`

echo "Edit inventory file and change/add below parameters"
echo"============================================================"
sudo sed  -i "s/python3/python/g" ~/awx/installer/inventory
sudo sed  -i "s/awxsecret/$secret_key/g" ~/awx/installer/inventory
sudo sed  -i "s/#project_data_dir/project_data_dir/g" ~/awx/installer/inventory
sudo sed  -i "s/host_port=80/host_port=8080/g" ~/awx/installer/inventory
sudo sed  -i "/#ssl_certificate=/a\\use_docker_compose=true" ~/awx/installer/inventory

echo "Install AWX"
echo "============================================================"
cd awx/installer/ 
ansible-playbook -i inventory install.yml

echo "============================================================"
echo "Install AWX cli"
echo "============================================================"
sudo pip install ansible-tower-cli

echo "AWX cli"
#configure AWX CLI
tower-cli config host  http://localhost:8080

#Set the privileged account for authenticating to Ansible Tower on Tower CLI
tower-cli config username admin

#Set the admin password on Tower CLI for your ansible tower/AWXinstance.
tower-cli config password password

#Set Verify SSL as false. (it might vary depending on your ansible Tower site protocal).
tower-cli config verify_ssl False

