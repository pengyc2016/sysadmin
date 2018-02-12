#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from UserManage.models import User


def selfpaginator(request, mlist, limit):
    """分页模块

    用法:
        1.view中引入：
        ex:from website.common.CommonPaginator import SelfPaginator
        
        2.SelfPaginator需要传入三个参数
            (1).request:获取请求数据
            (2).mlist:为需要分页的数据（一般为*.objects.all()取出来数据）
            (3).limit:为每页显示的条数
        ex:lst = SelfPaginator(request,mList, 5)
        
        3.view需要获取SelfPaginator return的lst，并把lst返回给前端模板
        ex:kwvars = {'lPage':lst,}
        
        4.前端需要for循环lPage也就是lst读取每页内容
        ex:{% for i in lPage %} ... {% endfor %}
        
        5.模板页引入paginator.html
        ex:{% include "common/paginator.html" %}
    """

    paginator = Paginator(mlist, int(limit))

    page = request.GET.get('page')
    try:
        lst = paginator.page(page)
    except PageNotAnInteger:
        lst = paginator.page(1)
    except EmptyPage:
        lst = paginator.page(paginator.num_pages)

    return lst

if __name__ == '__main__':
    rList = User.objects.all()
    lst = selfpaginator(request, rList, 20)
