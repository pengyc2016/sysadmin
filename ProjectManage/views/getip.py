#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ResourceManage.models import Vlan, VlanGroup
from ProjectManage.models import Vm, Cluster, Pm
from django.contrib.auth.decorators import login_required
from UserManage.views.permission import permissionverify
from django.http import JsonResponse
from IPy import IP
# import json


def sort_ip_list(ip_list):
    tmpip = [(IP(ip).int(), ip) for ip in ip_list]
    tmpip.sort()
    return [ip[1] for ip in tmpip]


@login_required
@permissionverify()
def get_ip(request):
        num = request.GET['num']
        pnum = request.GET['pnum']
        ipcount = int(request.GET['ipcount'])

        # 定义网段类型中所有ip地址列表
        list1 = []
        # 定义已使用ip地址列表
        list2 = []
        # 定义网段类型中可用ip地址列表
        # list3 = []
   
        if num != '':
            vlangroup_id = Cluster.objects.get(id=int(num)).vlangroup_id
        if pnum != '':
            vlangroup_id = Pm.objects.get(id=int(pnum)).vlangroup_id
        vlangroupobject = VlanGroup.objects.get(id=vlangroup_id)
        vlanqueryset = vlangroupobject.vlan.all()
        for obj in vlanqueryset:
            tmp_ip = obj.vlanname.rstrip().split('.')
            suffix_ip = tmp_ip[0]+'.'+tmp_ip[1]+'.'+tmp_ip[2]
            thestartip = obj.startip
            theendip = obj.endip
            for j in range(thestartip, theendip+1):
                ip = suffix_ip + '.' + str(j)
                list1.append(ip)
        ips = Vm.objects.values("ip")
        vips = Vm.objects.values("vip")
        scan = Vm.objects.values("scan")
        if ip != '':
            for i in ips:
                ip1 = i['ip']
                list2.append(ip1)
        if vips != '':
            for i in vips:
                vip1 = i['vip']
                list2.append(vip1)
        if scan != '':
            for i in scan:
                scan1 = i['scan']
                list2.append(scan1)
        set1 = set(list1)
        set2 = set(list2)
        set3 = set1-set2
        list3 = list(set(set3))
        iplist = sort_ip_list(list3)
        resultdict = {}
        ip_tmp = iplist[0].split('.')
        ip_suffix = ip_tmp[0]+'.'+ip_tmp[1]+'.'+ip_tmp[2]
        gateway = Vlan.objects.get(vlanname__contains=ip_suffix).gateway
        mask = Vlan.objects.get(vlanname__contains=ip_suffix).mask
        if ipcount == 1:
            resultdict['ip'] = iplist[0]
            resultdict['mask'] = mask
            resultdict['gateway'] = gateway
        elif ipcount == 2:
            resultdict['ip'] = iplist[0]
            resultdict['vip'] = iplist[1]
            resultdict['mask'] = mask
            resultdict['gateway'] = gateway
        elif ipcount == 3:
            resultdict['ip'] = iplist[0]
            resultdict['vip'] = iplist[1]
            resultdict['scanip'] = iplist[2]
            resultdict['mask'] = mask
            resultdict['gateway'] = gateway
        else:
            pass
        # return HttpResponse(json.dumps(resultdict),content_type='application/json')
        return JsonResponse(resultdict)
