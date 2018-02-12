#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from ProjectManage.forms import VmForm
from ProjectManage.models import Vm
from ProjectManage.models import Project
from ProjectManage.models import Pm
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify
from website.common.export import daochuvm
#from ProjectManage.views.getinfo import get_info
#from ProjectManage.views.getinfo import get_ping
from ProjectManage.views.ansible_interface import AnsiInterface
from ProjectManage.views.ansible_api import AnsibleAPI
from django.http import JsonResponse
import json


@permissionverify()
@login_required
def vm_input(request):
    """虚拟机录入"""
    if request.method == 'POST':
        form = VmForm(request.POST)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm()
        form.fields['pm'].queryset = Pm.objects.filter(role="物理单机宿主机")
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vm_list(request):
    """虚拟机展示"""
    mlist = Vm.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 10)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vm_delete(request, num):
    """虚拟机删除"""
    Vm.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('vmlist'))


@permissionverify()
@login_required
def vm_edit(request, num):
    """虚拟机编辑"""
    pj = Vm.objects.get(id=num)
    if request.method == 'POST':
        form = VmForm(request.POST, instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmedit.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vm_replication(request, num):
    """虚拟机复制"""
    pj = Vm.objects.get(id=num)
    if request.method == 'POST':
        form = VmForm(request.POST, instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vm_query(request):
    """虚拟机查询"""
    kwargs = {}
    vmname = request.GET.get('vmname')
    project = request.GET.get('project')
    ip = request.GET.get('ip')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if vmname != '':
        kwargs['vmname__icontains'] = vmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role__icontains'] = role
    if os != '':
        kwargs['os__icontains'] = os 
    if project != '':
            kwargs['project__projectname__icontains'] = project
    print kwargs
    mlist = Vm.objects.filter(**kwargs)
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def vm_export(request):
    """虚拟机信息导出"""
    kwargs = {}
    vmname = request.GET.get('vmname')
    project = request.GET.get('project')
    ip = request.GET.get('ip')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if vmname != '':
        kwargs['vmname__icontains'] = vmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role__icontains'] = role
    if os != '':
        kwargs['os__icontains'] = os 
    if project != '':
            kwargs['project__projectname__icontains'] = project
    fnstr = u'vm'
    if kwargs == {}:
        objs = Vm.objects.all()
    else:
        for k in kwargs:
            fnstr = fnstr+'_'+kwargs[k]
        objs = Vm.objects.filter(**kwargs)
    fn = fnstr+'.xls'
    return daochuvm(objs, fn)

@login_required
@permissionverify()
def vm_update(request, num):
    """虚拟机信息更新"""
    server = Vm.objects.get(id=num)
    resource = [{"hostname": server.ip, "port": "22", "username":"root","password": "pass", "ip": server.ip}]

    interface = AnsiInterface(resource)
    #connectstate = interface.exec_ping(server.ip)
    #if connectstate=='pong':
    cmdb_data = interface.handle_cmdb_data(server.ip)
    if cmdb_data:
        vmstatus = True
        for ds in cmdb_data:
            Vm.objects.filter(id=num).update(pycpu=ds.get('pycpu'),kernel=ds.get('kernel'),os=ds.get('os'),vmname=ds.get('vmname'),cpu=ds.get('cpu_count'),mem=ds.get('mem'),uptime=ds.get('uptime'),disk=ds.get('disktotal'),diskmount=ds.get('diskmount'),arch=ds.get('arch'),vmstatus=vmstatus)
        return JsonResponse({ "code":200,"msg":"更新成功", "ip":server.ip})
    else:
        #vmstatus = False
        #Vm.objects.filter(id=num).update(vmstatus=vmstatus) 
        return JsonResponse({ "code":500,"msg":"更新失败","ip":server.ip })
        #return HttpResponseRedirect(reverse('vmlist'))





