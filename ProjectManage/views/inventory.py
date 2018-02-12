#!/usr/bin/python
# -*- coding: utf-8 -*-

from ProjectManage.models import Vm, Project
# from django.contrib.auth.decorators import login_required
# from UserManage.views.permission import permissionverify
# from django.http import JsonResponse
#from ProjectManage.views.get_inv import dy_inv
import argparse
try:
  import json
except ImportError:
  import simplejson as json

def getList():
  inv_dict = {}
  projects = Project.objects.all()
  for project in projects:
    vmlist = []
    env = project.env
    shortname = project.shortname
    groupname = env + shortname
    vm = Vm.objects.filter(project=project).values("ip")
    if vm != '':
        for i in vm:
            ip1 = i['ip']
            vmlist.append(ip1)
    groupdata = {"hosts": vmlist}
    inv_dict[groupname] = groupdata
    return json.dumps(inv_dict)

def getVars(host):
  pass
#  print json.dumps(["vars"])



if __name__ == "__main__":
     parser = argparse.ArgumentParser()
     parser.add_argument('--list',action='store_true',dest='list',help='get all hosts')
     parser.add_argument('--host',action='store',dest='host',help='get all hosts')
     args = parser.parse_args()
     if args.list:
            getList()
     if args.host:
            getVars(args.host)
