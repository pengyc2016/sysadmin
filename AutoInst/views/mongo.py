# coding:utf8
import os
import hashlib
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from AutoInst.forms import MongoForm, MongoreplsetForm
from .common import command


@login_required
def mongo(request):
    if request.method == 'POST':
        form = MongoForm(request.POST)
        if form.is_valid():
            xx = form.cleaned_data
            master = xx['master']
            slave = xx['slave']
            mongoversion = xx['mongoversion']
            password = xx['password']
            allvm = master.split()+slave.split()
            print master
            print slave
            print allvm
            print mongoversion
            print password
            md5 = hashlib.md5(master).hexdigest()
            # mongo安装
            for ip in allvm:
                if ip in master.split():
                    mtype = "master"
                else:
                    mtype = "slave"
                cmd1 = " ".join(["/soft/QJZS/mongodb/mongo.sh ", mongoversion, master, mtype, md5])
                command(ip, password, cmd1)

            # mongo添加认证
            for ip in allvm:
                if ip in master.split():
                    mtype = "master"
                else:
                    mtype = "slave"
                cmd2 = " ".join(["/soft/QJZS/mongodb/mongo_priv.sh ", mongoversion, master, mtype])
                command(ip, password, cmd2)

            f = open('/tmp/out.txt')
            out = f.read()
            f.close()
            kwvars = {
               'form': form,
               'result': out,
            }
        # text="安装成功"
        return render(request, 'AutoInst/mongoForm.html', kwvars)
        # return HttpResponse(text)

    else:
        form = MongoForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('AutoInst/mongoForm.html', kwvars, RequestContext(request))
    # return render(request,'AutoInst/mongoForm.html',{'form':form})


@login_required
def mongoreplset(request):
    if request.method == 'POST':
        form = MongoreplsetForm(request.POST)
        if form.is_valid():
            xx = form.cleaned_data
            mongolist = xx['mongolist'].split()
            arbiter = xx['arbiter'].split()
            mongoversion = xx['mongoversion']
            password = xx['password']
            allvm = mongolist+arbiter
            print mongolist
            print arbiter
            print allvm
            print mongoversion
            print password
            md5 = hashlib.md5(password).hexdigest()
            # mongoreplset安装
            for ip in allvm:
                cmd1 = " ".join(["/soft/QJZS/mongodb/mongoreplset.sh ", mongoversion, md5])
                command(ip, password, cmd1)
            '''
            # mongo添加认证
            for ip in allvm:
                if ip in master.split():
                    mtype = "master"
                else:
                    mtype = "slave"
                cmd2 = " ".join(["/soft/QJZS/mongodb/mongo_priv.sh ", mongoversion, master, mtype])
                command(ip, password, cmd2)
            '''
            f = open('/tmp/out.txt')
            out = f.read()
            f.close()
            kwvars = {
               'form': form,
               'result': out,
            }
        # text="安装成功"
        return render(request, 'AutoInst/mongoreplsetForm.html', kwvars)
        # return HttpResponse(text)
    else:
        form = MongoreplsetForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('AutoInst/mongoreplsetForm.html', kwvars, RequestContext(request))
    # return render(request,'AutoInst/mongoreplsetForm.html',{'form':form})


@login_required
def mongohelp(request):
    return render_to_response('AutoInst/mongohelp.html', RequestContext(request))
