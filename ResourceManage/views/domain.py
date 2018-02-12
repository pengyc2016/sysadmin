#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import DomainForm
from ResourceManage.models import Domain
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify


@permissionverify()
@login_required
def domaininput(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('domainlist'))
    else:
        form = DomainForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/domainForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def domainlist(request):
    mlist = Domain.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request
    }
    return render_to_response('ResourceManage/domainlist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def domaindelete(request, num):
    Domain.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('domainlist'))


@permissionverify()
@login_required
def domainedit(request, num):
    cl = Domain.objects.get(id=num)

    if request.method == 'POST':
        form = DomainForm(request.POST, instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('domainlist'))
    else:
        form = DomainForm(instance=cl)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/domainedit.html', kwvars, RequestContext(request))




