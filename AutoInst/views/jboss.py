# coding:utf8
# import paramiko
import hashlib
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from AutoInst.forms import JbossForm
from .common import command


@login_required
def jboss(request):
    if request.method == 'POST':
        form = JbossForm(request.POST)
        if form.is_valid():
            xx = form.cleaned_data
            jbosslist = xx['jbosslist'].split()
            apachelist = xx['apachelist'].split()
            jbossversion = xx['jbossversion']
            sysname = xx['sysname']
            password = xx['password']
            install_apache = request.REQUEST.get('install_apache')
            password1 = 'pengyc'
            templist = ''
            # 生成jboss配置文件proxylist段字符串
            for ip in apachelist:
                str1 = ip + ':6660,'
                templist = templist+str1
            proxylist = templist[0:-1]
            # 地址后缀
            iptmp = jbosslist[0].rstrip().split('.')
            houzhui = iptmp[2]+'.'+iptmp[3]

            # 控制台密码转md5
            user = 'admin'
            passwd = sysname+'-12345'
            str1 = user+':ManagementRealm:'+passwd
            md5 = hashlib.md5(str1).hexdigest()

            # jboss安装
            for ip in jbosslist:
                cmd = " ".join(["/soft/QJZS/jboss/jboss1.sh ", jbossversion, houzhui, md5, proxylist])
                command(ip, password, cmd)
            # apache安装
            if install_apache == "yes":
                for ip in apachelist:
                    cmd = "sh /soft/QJZS/apache/apache.sh"
                    command(ip, password, cmd)
            f = open('/tmp/out.txt')
            out = f.read()
            f.close()
            # text=u"安装成功"
            kwvars = {
               'form': form,
               'result': out,
            }
        return render(request, 'AutoInst/jbossForm.html', kwvars)
        # return HttpResponse(text)
    else:
        form = JbossForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('AutoInst/jbossForm.html', kwvars, RequestContext(request))
    # return render(request,'AutoInst/jbossForm.html',{'form':form})


@login_required
def jbosshelp(request):
    return render_to_response('AutoInst/jbosshelp.html', RequestContext(request))
