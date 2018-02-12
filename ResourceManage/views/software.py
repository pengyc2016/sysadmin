#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import SoftwareForm
from ResourceManage.models import Software
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify


@permissionverify()
@login_required
def softwareinput(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            soft = form.save(commit=False)
            soft.softwarefullname = soft.softwarename+'_'+soft.version+'_'+soft.platform+'_'+soft.arch
            form.save()
            return HttpResponseRedirect(reverse('softwarelist'))
    else:
        form = SoftwareForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/softwareForm.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def softwarelist(request):
    mlist = Software.objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/softwarelist.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def softwaredelete(request, num):
    Software.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('softwarelist'))


@permissionverify()
@login_required
def softwareedit(request, num):
    soft = Software.objects.get(id=num)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=soft)
        if form.is_valid():
            soft = form.save(commit=False)
            soft.softwarefullname = soft.softwarename+'_'+soft.version+'_'+soft.platform+'_'+soft.arch
            form.save()
            return HttpResponseRedirect(reverse('softwarelist'))
    else:
        form = SoftwareForm(instance=soft)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/softwareedit.html', kwvars, RequestContext(request))


@permissionverify()
@login_required
def softwarequery(request):
    kwargs = {}
    softwarename = request.GET.get('softwarename')
    version = request.GET.get('version')
    platform = request.GET.get('platform')
    arch = request.GET.get('arch')
    softtype = request.GET.get('softtype')
    if softwarename != '':
        kwargs['softwarename__contains'] = softwarename 
    if version != '':
        kwargs['version__contains'] = version
    if platform != '':
        kwargs['platform__contains'] = platform 
    if arch != '':
        kwargs['arch__contains'] = arch
    if softtype != '':
        kwargs['softtype__contains'] = softtype
    mlist = Software.objects.filter(**kwargs)
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/softwarelist.html', kwvars, RequestContext(request))
