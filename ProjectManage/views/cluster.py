#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ProjectManage.forms import ClusterForm
from ProjectManage.models import Cluster, Vm, Pm
from ResourceManage.models import Storage, StorageGroup, VlanGroup
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify
from website.common.export import daochucluster


@permissionverify()
@login_required
def cluster_input(request):
    """录入集群信息"""
    if request.method == 'POST':
        form = ClusterForm(request.POST)
        if form.is_valid():
            cluster = form.save(commit=False)
            StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
            VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))
    else:
        form = ClusterForm()
        form.fields['vlangroup'].queryset = VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset = StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/clusterForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def cluster_list(request):
    """展示集群信息"""
    mlist = Cluster.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/clusterlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def cluster_delete(request, num):
    """删除集群信息"""
    cluster = Cluster.objects.filter(id=num)
    StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
    VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
    cluster.delete()
    return HttpResponseRedirect(reverse('clusterlist'))


@permissionverify()
@login_required
def cluster_edit(request, num):
    """编辑集群信息"""
    cl = Cluster.objects.get(id=num)
    StorageGroup.objects.filter(id=cl.storagegroup_id).update(is_selected=0)
    VlanGroup.objects.filter(id=cl.vlangroup_id).update(is_selected=0)
    if request.method == 'POST':
        form = ClusterForm(request.POST, instance=cl)
        if form.is_valid():
            cluster = form.save(commit=False)
            StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
            VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))
    else:
        form = ClusterForm(instance=cl)
        form.fields['vlangroup'].queryset = VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset = StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/clusteredit.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def cluster_show_pm(request, num):
    """显示选定集群对应物理机"""
    cl = Cluster.objects.get(id=num)
    mlist = cl.pm_set.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/pmlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def cluster_show_vm(request, num):
    """显示选定集群对应虚拟机"""
    cl = Cluster.objects.get(id=num)
    mlist = cl.vm_set.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def cluster_query(request):
    """集群信息查询"""
    kwargs = {}
    clustername = request.GET.get('clustername')
    platform = request.GET.get('platform')
    vcaddress = request.GET.get('vcaddress')
    if clustername != '':
        kwargs['clustername__contains'] = clustername 
    if platform != '':
        kwargs['platform__contains'] = platform 
    if vcaddress != '':
        kwargs['vcaddress__contains'] = vcaddress
    mlist = Cluster.objects.filter(**kwargs)
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/clusterlist.html', kwvars, RequestContext(request))
      

@login_required
@permissionverify()
def cluster_flush(request):
    """集群信息刷新"""
    tmpdict = {}
    idlist = []
    ids = Cluster.objects.values("id")
    for i in ids:
        num = i['id']
        idlist.append(num)
    for x in idlist:
        tmpdict[x] = Cluster.objects.get(id=x).storagegroup_id
    for num in tmpdict:
        ttcore = 0
        ttmem = 0
        ttstorage = 0
        usedcore = 0
        usedmem = 0
        usedstorage = 0
        storagegroup_id = tmpdict[num]
        pmqueryset = Pm.objects.filter(cluster_id=num)
        vmqueryset = Vm.objects.filter(cluster_id=num)
        storagequeryset = Storage.objects.filter(storagegroup_id=storagegroup_id)
        for i in pmqueryset:
            cpu = i.cpu
            mem = i.memory
            ttcore = ttcore+cpu
            ttmem = ttmem+mem

        for j in vmqueryset:
            cpu = j.cpu
            mem = j.mem
            disk = j.disk
            usedcore = usedcore+cpu
            usedmem = usedmem+mem
            usedstorage = usedstorage+disk
        for x in storagequeryset:
            storagesize = x.storagesize
            ttstorage = ttstorage+storagesize
        sycore = ttcore-usedcore
        symem = ttmem-usedmem
        systorage = ttstorage-usedstorage
        Cluster.objects.filter(id=num).update(ttstorage=ttstorage, systorage=systorage, usedstorage=usedstorage,
                                              ttcore=ttcore, sycore=sycore, usedcore=usedcore, ttmem=ttmem,
                                              symem=symem, usedmem=usedmem)
        StorageGroup.objects.filter(id=storagegroup_id).update(ttstorage=ttstorage, systorage=systorage,
                                                               usedstorage=usedstorage)
    mlist = Cluster.objects.all()
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/clusterlist.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def cluster_export(request):
    """集群信息导出"""
    kwargs = {}
    clustername = request.GET.get('clustername')
    platform = request.GET.get('platform')
    vcaddress = request.GET.get('vcaddress')
    if clustername != '':
        kwargs['clustername__contains'] = clustername 
    if platform != '':
        kwargs['platform__contains'] = platform 
    if vcaddress != '':
        kwargs['vcaddress__contains'] = vcaddress 
    fnstr = u'cluster'
    if kwargs == {}:
        objs = Cluster.objects.all()
    else: 
        for k in kwargs:
            fnstr = fnstr+'_'+kwargs[k]
        objs = Cluster.objects.filter(**kwargs)
    fn = fnstr+'.xls'
    return daochucluster(objs, fn)





