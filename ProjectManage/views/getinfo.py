#!/usr/bin/python
# -*- coding: utf-8 -*-
import ansible.runner
from ansible.inventory import Inventory
# from ProjectManage.views.get_inv import dy_inv
#from ProjectManage.views.inventory import *
#hostfile='/etc/ansible/hosts'

def get_info(ip):
    data = {}
    runner = ansible.runner.Runner(module_name='setup', module_args='', pattern=ip, forks=2)
    datastructure = runner.run()
    hostname = datastructure['contacted'][ip]['ansible_facts']['ansible_hostname']
    ansible_machine = datastructure['contacted'][ip]['ansible_facts']['ansible_machine']
    os_kernel = datastructure['contacted'][ip]['ansible_facts']['ansible_kernel']
    cpu_count = datastructure['contacted'][ip]['ansible_facts']['ansible_processor_count']
    cpu_core = datastructure['contacted'][ip]['ansible_facts']['ansible_processor_cores']
    mem = round(datastructure['contacted'][ip]['ansible_facts']['ansible_memtotal_mb']/1024.0)
    ipaddr = datastructure['contacted'][ip]['ansible_facts']['ansible_all_ipv4_addresses'][0]

    disktotal = sum([int(datastructure['contacted'][ip]['ansible_facts']["ansible_devices"][i]["sectors"])*   \
                     int(datastructure['contacted'][ip]['ansible_facts']["ansible_devices"][i]["sectorsize"])/1024/1024\
                     for i in datastructure['contacted'][ip]['ansible_facts']["ansible_devices"] \
                     if i[0:2] in ("sd", "ss")])
    diskmount = str({i["mount"]: i["size_total"]/1024/1024/1024.0 for i in \
                     datastructure['contacted'][ip]['ansible_facts']["ansible_mounts"]})
    uptime = datastructure['contacted'][ip]['ansible_facts']['facter_uptime']
    os = datastructure['contacted'][ip]['ansible_facts']['facter_os']['lsb']['distdescription']
    
    data['hostname'] = hostname
    data['ansible_machine'] = ansible_machine
    data['os_kernel'] = os_kernel
    data['cpu_count'] = cpu_count
    data['cpu_core'] = cpu_core
    data['mem'] = mem
    data['ipaddr'] = ipaddr
    data['disktotal'] = disktotal/1024.00
    data['diskmount'] = diskmount
    data['uptime'] = uptime
    data['os'] = os
    
    return data
    if __name__ == '__main__':
        data = get_info('')


def get_ping(ip):
    data = {}
    runner = ansible.runner.Runner(host_list=hostfile, module_name='ping', module_args='', pattern='all', forks=2)
    datastructure = runner.run()
    ping = datastructure['contacted'][ip]['ping']
    data['ping'] = ping
    
    return data
    if __name__ == '__main__':
        data = get_ping('')







