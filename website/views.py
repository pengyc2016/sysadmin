#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ResourceManage.models import Tongji, Storage, Software
from ProjectManage.models import Vm, Pm, Cluster, Project
import json


@login_required
def home(request):
    # 建表
    """
    Tongji.objects.all().delete()
    typelist = ["搭建项目", "物理机总数", "虚拟机总数", "存储总数", "集群总数", "CPU总核数","内存总数",
                "虚拟机已用CPU总核数", "虚拟机已用内存总数", "虚拟机已用存储总数", "软件总数","单机宿主物理机",
                "集群宿主物理机", "物理单机",  "Linux虚拟机", "Windows虚拟机","其他类型虚拟机"
                ]
    for i in typelist:
        p = Tongji(tongjitype=i, count=0)
        p.save()
    """
    # 统计
    totalproject = Project.objects.count()
    totalvm = Vm.objects.count()
    totalpm = Pm.objects.count()
    totalcluster = Cluster.objects.count()
    totalsoft = Software.objects.count()
    jqszpm = Pm.objects.filter(role="物理集群宿主机").count()
    djszpm = Pm.objects.filter(role="物理单机宿主机").count()
    djpm = Pm.objects.filter(role="物理单机").count()
    winvm = Vm.objects.filter(os__contains="WINDOW").count()
    lnxvm = Vm.objects.filter(os__contains="RHEL").count()
    qtvm = totalvm-winvm-lnxvm
    totalstorage = 0
    totalcpu = 0
    totalmem = 0
    usedtotalcpu = 0
    usedtotalmem = 0
    usedtotalstorage = 0
    for b in Pm.objects.values("cpu"):
        cpucount = b['cpu']
        totalcpu = totalcpu+cpucount
    for c in Vm.objects.values("cpu"):
        usedcpucount = c['cpu']
        usedtotalcpu = usedtotalcpu+usedcpucount
    for d in Vm.objects.values("mem"):
        usedmemcount = d['mem']
        usedtotalmem = usedtotalmem+usedmemcount
    for e in Vm.objects.values("disk"):
        usedstoragecount = e['disk']
        usedtotalstorage = usedtotalstorage+usedstoragecount
    for f in Pm.objects.values("memory"):
        memcount = f['memory']
        totalmem = totalmem+memcount
    for g in Storage.objects.values("storagesize"):
        storagecount = g['storagesize']
        totalstorage = totalstorage+storagecount

    # 统计存表
    Tongji.objects.filter(tongjitype="搭建项目").update(count=totalproject) 
    Tongji.objects.filter(tongjitype="物理机总数").update(count=totalpm) 
    Tongji.objects.filter(tongjitype="虚拟机总数").update(count=totalvm) 
    Tongji.objects.filter(tongjitype="存储总数").update(count=totalstorage)
    Tongji.objects.filter(tongjitype="集群总数").update(count=totalcluster)
    Tongji.objects.filter(tongjitype="CPU总核数").update(count=totalcpu)
    Tongji.objects.filter(tongjitype="内存总数").update(count=totalmem)
    Tongji.objects.filter(tongjitype="虚拟机已用CPU总核数").update(count=usedtotalcpu)
    Tongji.objects.filter(tongjitype="虚拟机已用内存总数").update(count=usedtotalmem)
    Tongji.objects.filter(tongjitype="虚拟机已用存储总数").update(count=usedtotalstorage)
    Tongji.objects.filter(tongjitype="软件总数").update(count=totalsoft)
    Tongji.objects.filter(tongjitype="单机宿主物理机").update(count=djszpm)
    Tongji.objects.filter(tongjitype="集群宿主物理机").update(count=jqszpm)
    Tongji.objects.filter(tongjitype="物理单机").update(count=djpm)
    Tongji.objects.filter(tongjitype="Windows虚拟机").update(count=winvm)
    Tongji.objects.filter(tongjitype="Linux虚拟机").update(count=lnxvm)
    Tongji.objects.filter(tongjitype="其他类型虚拟机").update(count=qtvm)
    # 获取表对象
    project = Tongji.objects.get(tongjitype="搭建项目").count
    pm = Tongji.objects.get(tongjitype="物理机总数").count
    vm = Tongji.objects.get(tongjitype="虚拟机总数").count
    storage = Tongji.objects.get(tongjitype="存储总数").count
    mem = Tongji.objects.get(tongjitype="内存总数").count
    cpu= Tongji.objects.get(tongjitype="CPU总核数").count
    cluster = Tongji.objects.get(tongjitype="集群总数").count
    usedcpu = Tongji.objects.get(tongjitype="虚拟机已用CPU总核数").count
    usedmem = Tongji.objects.get(tongjitype="虚拟机已用内存总数").count
    usedstorage = Tongji.objects.get(tongjitype="虚拟机已用存储总数").count
    systorage = storage-usedstorage
    sycpu = cpu-usedcpu
    symem = mem-usedmem
    soft = Tongji.objects.get(tongjitype="软件总数").count
    djszwlj = Tongji.objects.get(tongjitype="单机宿主物理机").count
    jqszwlj = Tongji.objects.get(tongjitype="集群宿主物理机").count
    wldj = Tongji.objects.get(tongjitype="物理单机").count
    linux = Tongji.objects.get(tongjitype="Linux虚拟机").count
    windows = Tongji.objects.get(tongjitype="Windows虚拟机").count
    othervm = Tongji.objects.get(tongjitype="其他类型虚拟机").count
    Dict = {
        'project': project,
        'pm': pm,
        'vm': vm,
        'cluster': cluster,
        'storage': storage,
        'cpu': cpu,
        'mem': mem,
        'usedstorage': usedstorage,
        'usedcpu': usedcpu,
        'usedmem': usedmem,
        'soft': soft,
        'djszwlj': djszwlj,
        'jqszwlj': jqszwlj,
        'wldj': wldj,
        'linux': linux,
        'windows': windows,
        'othervm': othervm,
        'systorage': systorage,
        'sycpu': sycpu,
        'symem': symem,
    }

    # return render_to_response('home.html',kwvars,RequestContext(request))
    return render(request, 'home.html', {'Dict': json.dumps(Dict)})
