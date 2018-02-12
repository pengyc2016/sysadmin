#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import VlanGroupForm
from ResourceManage.models import VlanGroup
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify


@permissionverify()
@login_required
def vlangroupinput(request):
    if request.method == 'POST':
        form = VlanGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlangrouplist'))
    else:
        form = VlanGroupForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangroupForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vlangrouplist(request):
    mlist = VlanGroup.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangrouplist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def vlangroupdelete(request, num):
    VlanGroup.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('vlangrouplist'))


@permissionverify()
@login_required
def vlangroupedit(request, num):
    cl = VlanGroup.objects.get(id=num)
    if request.method == 'POST':
        form = VlanGroupForm(request.POST, instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlangrouplist'))
    else:
        form = VlanGroupForm(instance=cl)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangroupedit.html', kwvars, RequestContext(request))




