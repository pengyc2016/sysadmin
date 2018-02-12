#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify
from UserManage.forms import RoleListForm
from UserManage.models import RoleList


@login_required
@permissionverify()
def addrole(request):
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/role.add.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def listrole(request):
    mlist = RoleList.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('UserManage/role.list.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def editrole(request, num):
    irole = RoleList.objects.get(id=num)
    if request.method == "POST":
        form = RoleListForm(request.POST, instance=irole)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroleurl'))
    else:
        form = RoleListForm(instance=irole)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/role.edit.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def deleterole(request,num):
    RoleList.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('listroleurl'))
