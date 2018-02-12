# coding:utf8
# import paramiko
# import os
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from AutoInst.forms import ZookeeperForm
from .common import command


@login_required
def zookeeper(request):
    if request.method == 'POST':
        form = ZookeeperForm(request.POST)
        if form.is_valid():
            xx = form.cleaned_data
            zookeeperlist = xx['zookeeperlist'].split()
            zookeeperversion = xx['zookeeperversion']
            password = xx['password']
            # print zookeeperlist
            # print zookeeperversion
            # print password
            string1 = ''
            zid = 1
            xx = 1
            # 生成zookeeper配置文件server段字符串
            for zk in zookeeperlist:
                str1 = 'server.' + str(xx) + '=' + zk + ':2888:3888i'
                string1 = string1+str1
                xx += 1
                # zookeeper安装
            for zk1 in zookeeperlist:
                myid = str(zid)
                cmd = " ".join(["/soft/QJZS/zookeeper/zookeeper.sh ", zookeeperversion,myid,string1])
                command(zk1, password, cmd)
                zid += 1
            f = open('/tmp/out.txt')
            out = f.read()
            f.close()
            # text=u"安装成功"
            kwvars = {
                'form': form,
                'result': out,
            }
            return render(request, 'AutoInst/zookeeperForm.html', kwvars)
            # return HttpResponse(text)
    else:
        form = ZookeeperForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('AutoInst/zookeeperForm.html', kwvars, RequestContext(request))
    # return render(request,'AutoInst/zookeeperForm.html',{'form':form})


@login_required
def zookeeperhelp(request):
    return render_to_response('AutoInst/zookeeperhelp.html', RequestContext(request))
