#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response , RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import selfpaginator
from UserManage.views.permission import permissionverify
from ProjectManage.models import Project
from UserManage.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from UserManage.forms import LoginUserForm, ChangePasswordForm, AddUserForm, EditUserForm


def loginuser(request):
    """用户登录view"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'GET' and request.GET. has_key('next'):
        next = request.GET['next']
    else:
        next = '/'

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(request.POST['next'])
    else:
        form = LoginUserForm(request)

    kwvars = {
        'request': request,
        'form': form,
        'next': next,
    }

    return render_to_response('UserManage/login.html', kwvars, RequestContext(request))


@login_required
def logoutuser(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def changepassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logouturl'))
    else:
        form = ChangePasswordForm(user=request.user)
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/password.change.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def listuser(request):
    mlist = get_user_model().objects.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('UserManage/user.list.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def adduser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = AddUserForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/user.add.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def edituser(request, num):
    user = get_user_model().objects.get(id=num)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listuserurl'))
    else:
        form = EditUserForm(instance=user)
    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/user.edit.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def deleteuser(request, num):
    if num == '1':
        return HttpResponse(u'超级管理员不允许删除!!!')
    else:
        get_user_model().objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('listuserurl'))


@login_required
@permissionverify()
def resetpassword(request, num):
    user = get_user_model().objects.get(id=num)
    newpassword = get_user_model().objects.make_random_password(length=10,
                                                                allowed_chars=
                                                                'abcdefghjklmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789')
    print '====>ResetPassword:%s-->%s' % (user.username, newpassword)
    user.set_password(newpassword)
    user.save()
    kwvars = {
        'object': user,
        'newpassword': newpassword,
        'request': request,
    }
    return render_to_response('UserManage/password.reset.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def showproject(request, num):
    theuser = User.objects.get(id=num)
    mlist = theuser.project_set.all()
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/projectlist.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def showvm(request, num):
    project_id_list = []
    mlist = []
    theuser = User.objects.get(id=num)
    projectlist = theuser.project_set.all()
    for i in projectlist:
        a = i.id
        project_id_list.append(a)
    for j in project_id_list:
        pj = Project.objects.get(id=j)
        vmlist = list(pj.vm_set.all())
        mlist = mlist + vmlist
    # 分页功能
    lst = selfpaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))
