# -*- coding:utf-8 -*-
import json
from ProjectManage.views.ansible_api import AnsibleAPI


class AnsiInterface(AnsibleAPI):
    def __init__(self, resource, *args, **kwargs):
        super(AnsiInterface, self).__init__(resource, *args, **kwargs)

    @staticmethod
    def deal_result(info):
        host_ips = info.get('success').keys()
        info['success'] = host_ips

        error_ips = info.get('failed')
        error_msg = {}
        for key, value in error_ips.items():
            temp = {}
            temp[key] = value.get('stderr')
            error_msg.update(temp)
        info['failed'] = error_msg
        return json.dumps(info)

    def copy_file(self, host_list, src=None, dest=None):
        """
        copy file
        """
        module_args = "src=%s  dest=%s"%(src, dest)
        self.run(host_list, 'copy', module_args)
        result = self.get_result()
        return self.deal_result(result)

    def exec_command(self, host_list, cmds):
        """
        commands
        """
        self.run(host_list, 'command', cmds)
        result = self.get_result()
        return self.deal_result(result)

    def exec_script(self, host_list, path):
        """
        在远程主机执行shell命令或者.sh脚本
        """
        self.run(host_list, 'shell', path)
        result = self.get_result()
        return self.deal_result(result)


    def exec_setup(self, host_list):
        """
        commands
        """
        self.run(host_list, 'setup')
        result = self.get_result()
        return self.deal_result(result)

    def exec_ping(self, host_list):
        """
        ping 
        """
        self.run(host_list, 'ping')
        result = self.get_result()
        data='xxx'
        for k, v in json.loads(json.dumps(result)).items():
            if k == "success":
                for x, y in v.items():
                    data=y.get('ping')
        return data


    def exec_setup_2(self, host_list):
        """
        commands
        """
        self.run(host_list, 'setup')
        result = self.get_result()
        return result



    def handle_cmdb_data(self, host_list):
        self.run(host_list, 'setup')
        result = self.get_result()
        data_list = []
        for k, v in json.loads(json.dumps(result)).items():
            if k == "success":
                for x, y in v.items():
                    cmdb_data = {}
                    data = y.get('ansible_facts')
                    disk_size = 0
                    cpu = data['ansible_processor'][-1]
                    for k, v in data['ansible_devices'].items():
                        if k[0:2] in ['sd', 'hd', 'ss', 'vd']:
                            disk = int((int(v.get('sectors')) * int(v.get('sectorsize'))) / 1024 / 1024 / 1024)
                            disk_size = disk_size + disk
                    cmdb_data['serial'] = data['ansible_product_serial'].split()[0]
                    cmdb_data['ip'] = x
                    cmdb_data['cpu'] = cpu.replace('@', '')
                   # ram_total = str(data['ansible_memtotal_mb'])
                   #if len(ram_total) == 4:
                   #     ram_total = ram_total[0] + 'GB'
                   # elif len(ram_total) == 5:
                   #     ram_total = ram_total[0:2] + 'GB'
                   # elif len(ram_total) > 5:
                   #     ram_total = ram_total[0:3] + 'GB'
                   # else:
                   #     ram_total = ram_total + 'MB'
                    cmdb_data['mem'] = data['ansible_memtotal_mb']
                    cmdb_data['disktotal'] = disk_size
                    cmdb_data['os'] = data['ansible_distribution'] + ' ' + data['ansible_distribution_version']
                    #cmdb_data['model'] = data['ansible_product_name'].split(':')[0]
                    cmdb_data['cpu_count'] = data['ansible_processor_vcpus']
                    #cmdb_data['vcpu_number'] = data['ansible_processor_vcpus']
                    cmdb_data['pycpu'] = data['ansible_processor_count']
                    cmdb_data['vmname'] = data['ansible_hostname']
                    cmdb_data['kernel'] = str(data['ansible_kernel'])
                    cmdb_data['arch'] = data['ansible_machine']
                    cmdb_data['ipaddr'] = data['ansible_all_ipv4_addresses'][0]
                    cmdb_data['diskmount'] = str({i["mount"]: i["size_total"]/1024/1024/1024.0 for i in data['ansible_mounts']})
                    uptime_seconds=data['ansible_uptime_seconds']
                    uptime_day=uptime_seconds/86400
                    uptime_hour=uptime_seconds%86400/3600
                    uptime_minute=uptime_seconds%86400%3600/60
                    uptime_second=uptime_seconds%86400%3600%60
                    cmdb_data['uptime'] = str(uptime_day)+'days'+ ', '+str(uptime_hour)+':'+str(uptime_minute)+':'+str(uptime_second)

                    #cmdb_data['manufacturer'] = data['ansible_system_vendor']
                    #if data['ansible_selinux']:
                    #    cmdb_data['selinux'] = data['ansible_selinux'].get('status')
                    #else:
                    #    cmdb_data['selinux'] = 'disabled'
                    #cmdb_data['swap'] = str(data['ansible_swaptotal_mb']) + 'MB'
                    #cmdb_data['status'] = 0
                    data_list.append(cmdb_data)
        if data_list:
            return data_list

