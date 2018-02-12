# coding:utf8
# import paramiko
# import os,hashlib
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from AutoInst.forms import ApacheForm
from .common import command


@login_required
def apache(request):
    if request.method == 'POST':
        form = ApacheForm(request.POST)
        if form.is_valid():
            xx = form.cleaned_data
            apachelist = xx['apachelist'].split()
            password = xx['password']
            print apachelist 
            print password 
            password1 = 'pengyc'
            # apache安装
            for ip in apachelist:
                cmd = "sh /soft/QJZS/apache/apache_single.sh"
                command(ip, password, cmd)
            f = open('/tmp/out.txt')
            out = f.read()
            f.close()
        # text="安装成功"
        kwvars = {
            'form': form,
            'result': out,
        }
        return render(request, 'AutoInst/apacheForm.html', kwvars)
        # return HttpResponse(text)
    else:
        form = ApacheForm()
        kwvars = {
            'form': form,
            'request': request,
        }
    return render_to_response('AutoInst/apacheForm.html', kwvars, RequestContext(request))
    # return render(request,'AutoInst/apacheForm.html',{'form':form})


@login_required
def apachehelp(request):
    return render_to_response('AutoInst/apachehelp.html', RequestContext(request))
