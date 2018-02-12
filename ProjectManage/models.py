#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from UserManage.models import User
from ResourceManage.models import Domain, VlanGroup, StorageGroup, Software


class Project(models.Model):
    env = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'环境')
    projectname = models.CharField(max_length=30, verbose_name=u'项目名称')
    shortname = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'项目简称')
    createuser = models.ForeignKey(User,blank=True, null=True, verbose_name=u'创建人员', on_delete=models.SET_NULL)
    starttime = models.DateTimeField(blank=True, null=True, verbose_name=u'项目开始时间')
    endtime = models.DateTimeField(blank=True, null=True, verbose_name=u'项目结束时间')
    finishtime = models.DateTimeField(blank=True, null=True, verbose_name=u'项目完成时间')
    reason = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'项目超时理由')
    batch = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'项目批次')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return '%s.%s' % (self.id, self.projectname)

    class Meta:
        db_table = 'project'
        ordering = ['-id']


class Cluster(models.Model):
    clustername = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u'集群名称')
    platform = models.CharField(max_length=30, verbose_name=u'集群平台')
    vcaddress = models.GenericIPAddressField(verbose_name=u'集群VC地址')
    vlangroup = models.ForeignKey(VlanGroup, null=True, verbose_name=u'集群网络组', on_delete=models.SET_NULL)
    storagegroup = models.ForeignKey(StorageGroup, null=True, verbose_name=u'集群存储组', on_delete=models.SET_NULL)
    ttstorage = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, verbose_name=u'集群存储')
    usedstorage = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True,
                                      verbose_name=u'集群已用存储')
    systorage = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True,
                                    verbose_name=u'集群剩余存储')
    ttcore = models.IntegerField(default=0, blank=True, verbose_name=u'集群CPU核数')
    usedcore = models.IntegerField(default=0, blank=True, verbose_name=u'集群已用CPU核数')
    sycore = models.IntegerField(default=0, blank=True, verbose_name=u'集群剩余CPU核数')
    ttmem = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, verbose_name=u'集群内存')
    usedmem = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, verbose_name=u'集群已用内存')
    symem = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, verbose_name=u'集群剩余内存')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.clustername

    class Meta:
        db_table = 'cluster'
        ordering = ['-id']
 

class Pm(models.Model):
    pmname = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u'物理机名称')
    sn = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机序列号')
    cluster = models.ForeignKey(Cluster, blank=True, null=True, verbose_name=u'物理机所属集群',
                                on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, blank=True, null=True, verbose_name=u'物理机所属项目',
                                on_delete=models.SET_NULL)
    vlangroup = models.ForeignKey(VlanGroup, blank=True, null=True, verbose_name=u'物理机所属网络组',
                                  on_delete=models.SET_NULL)
    storagegroup = models.ForeignKey(StorageGroup, blank=True, null=True, verbose_name=u'物理机所属存储组',
                                     on_delete=models.SET_NULL)
    role = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机角色')
    pmtype = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机类型')
    cpu = models.IntegerField(blank=True, null=True, verbose_name=u'物理机CPU核数')
    memory = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=u'物理机内存大小')
    disk = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=u'物理机磁盘大小')
    os = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机操作系统')
    soft = models.ForeignKey(Software, blank=True, null=True, verbose_name=u'物理机安装软件', on_delete=models.SET_NULL)
    eth = models.IntegerField(blank=True, null=True, verbose_name=u'物理机网卡个数')
    hba = models.IntegerField(blank=True, null=True, verbose_name=u'物理机HBA卡个数')
    ip = models.GenericIPAddressField(verbose_name=u'物理机地址')
    ilo_ip = models.GenericIPAddressField(verbose_name=u'物理机管理地址')
    mask = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'物理机子网掩码')
    gateway = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'物理机网关')
    domain = models.ForeignKey(Domain, blank=True, null=True, verbose_name=u'物理机所属域', on_delete=models.SET_NULL)
    jiguihao = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机机柜号')
    jiguiwei = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机机柜位')
    hba_wwn = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机HBA卡WWN')
    position = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'物理机位置')
    ttstorage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,
                                    verbose_name=u'物理机存储大小')
    systorage = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,
                                    verbose_name=u'剩余存储大小')
    sycore = models.IntegerField(blank=True, null=True, verbose_name=u'物理机剩余CPU核数')
    symem = models.IntegerField(blank=True, null=True, verbose_name=u'物理机剩余CPU核数')
    remark = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.pmname

    class Meta:
        db_table = 'pm'
        ordering = ['-id']


class Vm(models.Model):
    vmname = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=u'虚拟机名称')
    project = models.ForeignKey(Project, blank=True, null=True, verbose_name=u'所属项目', on_delete=models.SET_NULL)
    pm = models.ForeignKey(Pm,blank=True, null=True, verbose_name=u'所属物理机', on_delete=models.SET_NULL)
    role = models.CharField(max_length=30, blank=True,null=True, verbose_name=u'虚拟机角色')
    batch = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'虚拟机批次')
    env = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'虚拟机环境')
    cluster = models.ForeignKey(Cluster, blank=True, null=True, verbose_name=u'所属集群', on_delete=models.SET_NULL)
    os = models.CharField(max_length=80, verbose_name=u'虚拟机操作系统')
    soft = models.ForeignKey(Software, blank=True, null=True, verbose_name=u'虚拟机安装软件', on_delete=models.SET_NULL)
    cpu = models.IntegerField(blank=True, null=True, verbose_name=u'虚拟机逻辑cpu核数')
    mem = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True, verbose_name=u'虚拟机内存大小')
    disk = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True, verbose_name=u'虚拟机磁盘大小')
    ip = models.GenericIPAddressField(verbose_name=u'虚拟机地址')
    vip = models.GenericIPAddressField(verbose_name=u'虚拟机VIP地址', blank=True, null=True)
    scan = models.GenericIPAddressField(verbose_name=u'虚拟机SCAN地址', blank=True, null=True)
    mask = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'虚拟机子网掩码')
    gateway = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'虚拟机网关')
    domain = models.ForeignKey(Domain, blank=True, null=True, verbose_name=u'虚拟机所属域', on_delete=models.SET_NULL)
    admin = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'虚拟机管理员')
    appuser = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'虚拟机应用用户')
    uptime = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'虚拟机已启动时间')
    vmstatus = models.BooleanField(default=False, verbose_name=u'虚拟机开机状态')
    pycpu = models.IntegerField(blank=True, null=True, verbose_name=u'虚拟机物理cpu数')
    diskmount = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'磁盘挂载信息')
    kernel = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'系统内核版本')
    arch = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'系统架构')
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'备注')

    def __unicode__(self):
        return self.vmname

    class Meta:
        db_table = 'vm'
        ordering = ['-id']

