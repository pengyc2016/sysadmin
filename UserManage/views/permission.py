#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import selfpaginator
from UserManage.forms import PermissionListForm
from UserManage.models import User, RoleList, PermissionList


def permissionverify():
    """权限认证模块.

        此模块会先判断用户是否是管理员（is_superuser为True），如果是管理员，则具有所有权限,
        如果不是管理员则获取request.user和request.path两个参数，判断两个参数是否匹配，匹配则有权限，反之则没有。
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            iuser = User.objects.get(username=request.user)

            if not iuser.is_superuser:  # 判断用户如果是超级管理员则具有所有权限
                if not iuser.role:   # 如果用户无角色，直接返回无权限
                    return HttpResponseRedirect(reverse('permissiondenyurl'))
                role_permission = RoleList.objects.get(name=iuser.role)
                role_permission_list = role_permission.permission.all()

                matchurl = []
                for x in role_permission_list:
                    # 精确匹配，判断request.path是否与permission表中的某一条相符
                    if request.path == x.url or request.path.rstrip('/') == x.url:
                        matchurl.append(x.url)
                    # 判断request.path是否以permission表中的某一条url开头
                    elif request.path.startswith(x.url):
                        matchurl.append(x.url)
                    else:
                        pass
                print '%s---->matchurl:%s' % (request.user, str(matchurl))
                if len(matchurl) == 0:
                    return HttpResponseRedirect(reverse('permissiondenyurl'))
            else:
                pass
            return view_func(request, *args, **kwargs)
        return _wrapped_view

    return decorator


@login_required
def nopermission(request):

    kwvars = {
        'request': request,
    }
    return render_to_response('UserManage/permission.no.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def addpermission(request):
    if request.method == "POST":
        form = PermissionListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listpermissionurl'))
    else:
        form = PermissionListForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/permission.add.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def listpermission(request):
    mlist = PermissionList.objects.all()

    # 分页功能
    lst = selfpaginator(request, mlist, 20)

    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('UserManage/permission.list.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def editpermission(request, num):
    ipermission = PermissionList.objects.get(id=num)

    if request.method == "POST":
        form = PermissionListForm(request.POST, instance=ipermission)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listpermissionurl'))
    else:
        form = PermissionListForm(instance=ipermission)

    kwvars = {
        'num': num,
        'form': form,
        'request': request,
    }
    return render_to_response('UserManage/permission.edit.html', kwvars, RequestContext(request))


@login_required
@permissionverify()
def deletepermission(request, num):
    PermissionList.objects.filter(id=num).delete()
    return HttpResponseRedirect(reverse('listpermissionurl'))
