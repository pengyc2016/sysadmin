#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import VlanForm
from ResourceManage.models import Vlan
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify


@permissionverify()
@login_required
def vlaninput(request):
    if request.method == 'POST':
        form = VlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlanlist'))
    else:
        form = VlanForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlanForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vlanlist(request):
    mlist = Vlan.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/vlanlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vlandelete(request, num):
    Vlan.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('vlanlist'))


@permissionverify()
@login_required
def vlanedit(request, num):
    cl = Vlan.objects.get(id=num)
    if request.method == 'POST':
        form = VlanForm(request.POST, instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlanlist'))
    else:
        form = VlanForm(instance=cl)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlanedit.html', kwvars, RequestContext(request))




