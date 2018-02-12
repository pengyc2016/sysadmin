#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ProjectManage.forms import PmForm
from ProjectManage.models import Pm, Cluster
from ResourceManage.models import StorageGroup, VlanGroup
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify
from website.common.export import daochupm


@permissionverify()
@login_required
def pm_input(request):
    """物理机录入"""
    if request.method == 'POST':
        form = PmForm(request.POST)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role == u"物理单机宿主机":
                if pm.storagegroup_id != '':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.storagegroup_id != '':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role == u"物理单机":
                if pm.storagegroup_id != '':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id != '':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else:
                storagegroup_id = Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id = Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm()
        form.fields['vlangroup'].queryset = VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset = StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/pmForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def pm_list(request):
    """物理机展示"""
    mlist = Pm.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/pmlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def pm_delete(request, num):
    """物理机删除"""
    pm = Pm.objects.get(id=num)
    if pm.storagegroup_id != '':
        print pm.storagegroup_id
        StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=0)
    if pm.vlangroup_id != '':
        VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=0)
    pm.delete()
    return HttpResponseRedirect(reverse('pmlist'))


@permissionverify()
@login_required
def pm_edit(request, num):
    """物理机编辑"""
    bcpm = Pm.objects.get(id=num)
    if bcpm.storagegroup_id != '':
        StorageGroup.objects.filter(id=bcpm.storagegroup_id).update(is_selected=0)
    if bcpm.vlangroup_id != '':
        VlanGroup.objects.filter(id=bcpm.vlangroup_id).update(is_selected=0)
    if request.method == 'POST':
        form = PmForm(request.POST, instance=bcpm)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role == u"物理单机宿主机":
                StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role == u"物理单机":
                if pm.storagegroup_id != '':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id != '':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else:
                storagegroup_id = Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id = Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=bcpm)
        form.fields['vlangroup'].queryset = VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset = StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/pmedit.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def pm_replication(request, num):
    """物理机复制"""
    bcpm = Pm.objects.get(id=num)
    if bcpm.storagegroup_id != '':
        StorageGroup.objects.filter(id=bcpm.storagegroup_id).update(is_selected=0)
    if bcpm.vlangroup_id != '':
        VlanGroup.objects.filter(id=bcpm.vlangroup_id).update(is_selected=0)
    if request.method == 'POST':
        form = PmForm(request.POST, instance=bcpm)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role == u"物理单机宿主机":
                StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role == u"物理单机":
                if pm.storagegroup_id != '':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id != '':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else:
                storagegroup_id = Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id = Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=bcpm)
        form.fields['vlangroup'].queryset = VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset = StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/pmrepl.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def pm_query(request):
    """物理机信息查询"""
    kwargs = {}
    pmname = request.GET.get('pmname')
    ip = request.GET.get('ip')
    pmtype = request.GET.get('pmtype')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if pmname != '':
        kwargs['pmname__icontains'] = pmname
    if ip != '':
        kwargs['ip__contains'] = ip
    if role != '':
        kwargs['role__icontains'] = role
    if pmtype != '':
            kwargs['pmtype__icontains'] = pmtype
    if os != '':
        kwargs['os__icontains'] = os
    mlist = Pm.objects.filter(**kwargs)
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/pmlist.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def pm_export(request):
    """物理机信息导出"""
    kwargs = {}
    pmname = request.GET.get('pmname')
    ip = request.GET.get('ip')
    pmtype = request.GET.get('pmtype')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if pmname != '':
        kwargs['pmname__icontains'] = pmname
    if ip != '':
        kwargs['ip__contains'] = ip
    if role != '':
        kwargs['role__icontains'] = role
    if pmtype != '':
            kwargs['pmtype__icontains'] = pmtype
    if os != '':
        kwargs['os__icontains'] = os
    fnstr = u'pm'
    if kwargs == {}:
        objs = Pm.objects.all()
    else:
        for k in kwargs:
            fnstr = fnstr+'_'+kwargs[k]
        objs = Pm.objects.filter(**kwargs)
    fn = fnstr+'.xls'
    return daochupm(objs, fn)
