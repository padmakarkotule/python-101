#!/usr/bin/env python
import requests,json
import csv
import datetime
from ceph_report import Ceph

base_url = ""
admin_username = ""
admin_password = ""
admin_domain = ""
ceph_rest_api = ""


#Obtaining Keystone token

url = base_url + ':35357/v3/auth/tokens'
headers = {'content-type': 'application/json','Accept': 'application/json'}
da = {"auth": {"identity": {"methods": ["password"],"password": {"user": {"domain": {"name": admin_domain},"name": admin_username,"password": admin_password}}},"scope": {"project": {"domain": {"name": admin_domain},"name": admin_username}}}}
resp = requests.post(url, data=json.dumps(da), headers=headers)
loginData = json.loads(resp.text)
projectid = loginData['token']['project']['id']
token = resp.headers['X-Subject-Token']
#print projectid

#Obtaining Project List


url2 =  base_url +':35357/v3/projects/'
headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
resp = requests.get(url2, headers=headers)
projects = json.loads(resp.text)
#print projects



#removing service project
for i in range(0, len(projects['projects'])):
    if projects['projects'][i]['name'] == 'service':
       del projects['projects'][i]
       break
#print projects


#Actual Project usage details
nova_url =  base_url +':8774/v2.1/' + projectid

url3 = nova_url + '/os-simple-tenant-usage'
payload = {'detailed': '1'}
headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
resp = requests.get(url3,headers=headers,params=payload)
projects_usage = json.loads(resp.text)
#print projects_usage

#print projects_usage

for project in projects['projects']:
    for usage in projects_usage['tenant_usages']:
        if project['id'] == usage['tenant_id']:
            usagedata = {}
            total_vcpu = total_ram = total_disk = 0
            for server in usage['server_usages']:
                total_vcpu = total_vcpu + server['vcpus']
                total_ram = total_ram + server['memory_mb']
                total_disk = total_disk + server['local_gb']
            usagedata['total_vcpu'] = total_vcpu
            usagedata['total_ram'] = total_ram
            usagedata['total_disk'] = total_disk
            projects['usagedata'] = json.loads(json.dumps(usagedata))

#Obtaining number of users

for project in projects['project']:
    project_id = project['id']
    url =  base_url +':35357/v3/' + 'role_assignments/'
    payload = {'scope.project.id': project_id}
    headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
    resp = requests.get(url, headers=headers,params=payload)
    users = json.loads(resp.text)
    project['users'] = len(users['role_assignments'])




#Project Quota details

nova_url =  base_url +':8774/v2.1/' + projectid

for project in projects['project']:
    project_id = project['id']
    url = nova_url + '/os-quota-sets/'+project_id +'/detail'
    headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
    resp = requests.get(url, headers=headers)
    quota = json.loads(resp.text)
    project['quota'] = quota

#print projects





#Obtaining cinder Quota

cinder_url =  base_url +':8776/v2/' + projectid

for project in projects['projects']:
    project_id = project['id']
    url = cinder_url + '/os-quota-sets/'+project_id
    headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
    resp = requests.get(url, headers=headers)
    quota = json.loads(resp.text)
    project['cinder_quota'] = quota
    #import pdb; pdb.set_trace()


#Obtaining cinder usage

cinder_url =  base_url +':8776/v2/' + projectid

url4 = cinder_url + '/volumes/detail'
payload = {'all_tenants': '1'}
headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
resp = requests.get(url4,headers=headers,params=payload)
cinder_usage = json.loads(resp.text)

#print cinder_usage

for project in projects['projects']:
    volumes = 0
    size = 0
    for usage in cinder_usage['volumes']:
        if project['id'] == usage['os-vol-tenant-attr:tenant_id']:
           volumes = volumes + 1
           size = size + usage['size']
    project['volumes'] = volumes
    project['cinder_disk'] = size

#print projects

#for hypervisor status
url5 = nova_url + '/os-hypervisors/detail'
headers = {'content-type': 'application/json', 'User-Agent': 'python-novaclient', 'Accept': 'application/json','X-Auth-Token':token}
resp = requests.get(url5,headers=headers)
hypervisors = json.loads(resp.text)
#print hypervisors

def unitconvert(num):
    ans = num/float(1024)
    if ans.is_integer():
        return int(ans)
    else:
        return round(ans,2)


#creating csv file

now = datetime.datetime.now()
date = str(now.day)+"-"+str(now.month)+"-"+str(now.year)

f = open("reports/openstack_usage_report_"+date+".csv", "wb+")
reportfile = csv.writer(f)

reportfile.writerow(["Project Name","VCPUs", "RAM(GB)", "Disk(GB)", "No of Instances", "No of Volumes", "Cinder Storage(GB)", "No of Users"])

openstack_total_projects = len(projects['projects'])
openstack_total_users = 0
for pr in projects['projects']:
    if 'usagedata' in pr:
        disk = pr['usagedata']['total_disk']
    else:
        disk = 0

    core_inuse = pr['quota']['quota_set']['cores']['in_use']
    core_quota = pr['quota']['quota_set']['cores']['limit']
    ram_inuse = unitconvert(pr['quota']['quota_set']['ram']['in_use'])
    ram_quota = unitconvert(pr['quota']['quota_set']['ram']['limit'])
    instance_inuse = pr['quota']['quota_set']['instances']['in_use']
    instance_quota = pr['quota']['quota_set']['instances']['limit']
    openstack_total_users = openstack_total_users + pr['users']

    reportfile.writerow([pr['name'],str(core_inuse)+"/" +str(core_quota),str(ram_inuse)+"/" +str(ram_quota),disk,str(instance_inuse)+"/" +str(instance_quota), str(pr['volumes'])+"/" +str(pr['cinder_quota']['quota_set']['volumes']), str(pr['cinder_disk'])+"/" +str(pr['cinder_quota']['quota_set']['gigabytes']),pr['users'] ])


reportfile.writerow([])
reportfile.writerow([])
reportfile.writerow(["Hypervisor Details"])
reportfile.writerow(["Hypervisor name","Hypervisor IP","Instances","VCPUs Used","VCPUs Capacity","RAM in Use(GB)-OverCommited","RAM Capacity(GB)-OverCommited","Actual RAM(GB)","Disk Used(TB)","Total Disk(TB)","CPU Cores"])

openstack_instaces = 0
openstack_vcpu_used = 0
openstack_vcpu_capacity = 0
openstack_ram_used = 0
openstack_ram_capacity = 0
actual_ram_capacity = 0
openstack_disk_usage = 0
openstack_disk_capacity = 0

for h in hypervisors['hypervisors']:
     cores = h['vcpus']
     vcpu_capacity = cores * 4
     ram_capacity = h["memory_mb"] * 1.5

     openstack_instaces = openstack_instaces + h["running_vms"]
     openstack_vcpu_used = openstack_vcpu_used + h["vcpus_used"]
     openstack_vcpu_capacity = openstack_vcpu_capacity + vcpu_capacity
     openstack_ram_used = openstack_ram_used + h["memory_mb_used"]
     openstack_ram_capacity = openstack_ram_capacity + ram_capacity
     actual_ram_capacity = actual_ram_capacity + h["memory_mb"]
     openstack_disk_usage =openstack_disk_usage+  h["local_gb_used"]
     openstack_disk_capacity = openstack_disk_capacity + h["local_gb"]


     reportfile.writerow([h["hypervisor_hostname"],h["host_ip"],h["running_vms"],h["vcpus_used"],vcpu_capacity,unitconvert(h["memory_mb_used"]),unitconvert(ram_capacity),unitconvert(h["memory_mb"]),unitconvert(h["local_gb_used"]),unitconvert(h["local_gb"]),cores])


ceph = Ceph(ceph_rest_api)
c_status = ceph.get_status()
if c_status['Success']:
    reportfile.writerow([""])
    reportfile.writerow([""])
    reportfile.writerow(["CEPH Storage"])
    reportfile.writerow(["Ceph Status", "Used Storage(TB)","Available Storage(TB)","Total Storage(TB)","Physical Storage(TB)"])
    reportfile.writerow([c_status['status'],c_status['bytes_used'],c_status['bytes_available']/3,c_status['bytes_used']+c_status['bytes_available']/3,c_status['total_bytes']])

reportfile.writerow([])
reportfile.writerow([])
reportfile.writerow(["Overall Statistics"])
reportfile.writerow(["Total No of Users", openstack_total_users ])
reportfile.writerow(["Total No of Projects", openstack_total_projects ])
reportfile.writerow(["Total Running VMs", openstack_instaces  ])
reportfile.writerow(["Total VCPUs Used", openstack_vcpu_used ])
reportfile.writerow(["Total VCPUs Capacity", openstack_vcpu_capacity ])
reportfile.writerow(["Total RAM Used(GB)", unitconvert(openstack_ram_used) ])
reportfile.writerow(["Total RAM Capacity(GB)", unitconvert(openstack_ram_capacity) ])
reportfile.writerow(["Actual RAM of Setup(GB)", unitconvert(actual_ram_capacity) ])
reportfile.writerow(["Total Disk Usage(TB)", unitconvert(openstack_disk_usage)])
reportfile.writerow(["Total Disk Capacity(TB)", unitconvert(openstack_disk_capacity)])

f.close()
print "Report generated succesfully."
