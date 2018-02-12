#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from ProjectManage.models import Project, Vm, Cluster, Pm
# from ResourceManage.models import Software,Domain
# 环境选项
ENV_CHOICES = (('', '---------'),
               ('T1', 'T1'),
               ('T2', 'T2'),
               ('T3', 'T3'),
               ('T4', 'T4'),
               ('T5', 'T5'),
               ('X1', 'X1')
               )


# 平台选项
PLATFORM_CHOICES = (('', '---------'),
                    ('VSPHERE', 'VSPHERE'),
                    ('Hyper-V', 'Hyper-V'),
                    ('Window', 'Window'),
                    ('Linux', 'Linux'),
                    ('Aix', 'Aix'),
                    ('All', 'All'),
                    ('Other', 'Other')
                    )
# Vcenter选项
VC_IP_CHOICES = (('', '---------'),
                 ('22.188.18.231', '22.188.18.231'),
                 ('61.0.128.194', '61.0.128.194'),
                 ('61.0.128.200', '61.0.128.200'),
                 ('61.0.128.8', '61.0.128.8')
                 )


# 架构选项
ARCH_CHOICES = (('', '---------'),
                ('X86', 'X86'),
                ('X86_64', 'X86_64'),
                ('NOARCH', 'NOARCH')
                )

# 软件类型选项
TYPE_CHOICES = (('', '---------'),
                ('中间件', '中间件'),
                ('操作系统', '操作系统'),
                ('数据库', '数据库'),
                ('其他', '其他')
                )
# 批次选项
BATCH_CHOICES = (('', '---------'),
                 ('X601', 'X601'),
                 ('P604', 'P604'),
                 ('P605', 'P605'),
                 ('P606', 'P606'),
                 ('P701', 'P701'),
                 ('其他', '其他')
                 )

# 操作系统选项
OS_CHOICES = (('', '---------'),
              ('WINDOW SERVER 2003', 'WINDOW SERVER 2003'),
              ('WINDOW SERVER 2008', 'WINDOW SERVER 2008'),
              ('WINDOW SERVER 2008R2', 'WINDOW SERVER 2008R2'),
              ('WINDOW SERVER 2012', 'WINDOW SERVER 2012'),
              ('WINDOW SERVER 2012R2', 'WINDOW SERVER 2012R2'),
              ('RedHat 6.4', 'RedHat 6.4'),
              ('RedHat 6.6', 'RedHat 6.8'),
              ('RedHat 6.7', 'RedHat 6.7'),
              ('RedHat 6.8', 'RedHat 6.8'),
              ('RedHat 6.9', 'RedHat 6.9'),
              ('RedHat 7.3', 'RedHat 7.3'),
              ('RedHat 6.1', 'RedHat 6.1'),
              ('RedHat 5.4', 'RedHat 5.4'),
              ('ESXI5.5', 'ESXI5.5'),
              ('ESXI6.0', 'ESXI6.0'),
              ('other', 'other')
              )

# 机房位置选项
POSITION_CHOICES = (('', '---------'),
                    ('2C', '2C'),
                    ('2B', '2B')
                    )

# 物理机角色选项
ROLE_CHOICES = (('', '---------'),
                ('物理单机', '物理单机'),
                ('物理集群宿主机', '物理集群宿主机'),
                ('物理单机宿主机', '物理单机宿主机')
                )

# 虚拟机角色选项
VMROLE_CHOICES = (('', '---------'),
                  ('WEB服务器', 'WEB服务器'),
                  ('数据库服务器', '数据库服务器'),
                  ('应用服务器', '应用服务器'),
                  ('前置机', '前置机'),
                  ('其他', '其他')
                  )

# 掩码选项
MASK_CHOICES = (('', '---------'),
                ('255.255.255.0', '255.255.255.0'),
                ('255.255.255.128', '255.255.255.128'),
                ('255.255.0.0', '255.255.0.0')
                )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('env', 'shortname', 'projectname', 'createuser', 'starttime', 'endtime', 'finishtime', 'reason',
                  'batch', 'remark')
        widgets = {
            'env': forms.Select(),
            'shortname': forms.TextInput(),
            'projectname': forms.TextInput(),
            'createuser': forms.Select(),
            'starttime': forms.DateTimeInput(),
            'endtime': forms.DateTimeInput(),
            'finishtime': forms.DateTimeInput(),
            'reason': forms.Textarea(attrs={'cols': 120, 'rows': 2}),
            'batch': forms.Select(),
            'remark': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['env'].label = u'环境'
        self.fields['env'].widget.choices = ENV_CHOICES
        self.fields['env'].widget.attrs = {'class': 'form-control'}
        self.fields['shortname'].label = u'项目简称'
        self.fields['shortname'].widget.attrs = {'class': 'form-control'}
        self.fields['projectname'].label = u'项目名称'
        self.fields['projectname'].error_messages = {'required': u'请输入项目名称'}
        self.fields['projectname'].widget.attrs = {'class': 'form-control'}
        self.fields['createuser'].label = u'搭建人员'
        self.fields['createuser'].widget.attrs = {'class': 'form-control'}
        self.fields['starttime'].label = u'达到时间'
        self.fields['starttime'].widget.attrs = {'class': 'form-control form_datetime', 'readonly': 'True'}
        self.fields['endtime'].label = u'截止时间'
        self.fields['endtime'].widget.attrs={'class': 'form-control form_datetime', 'readonly': 'True'}
        self.fields['finishtime'].label = u'完成时间'
        self.fields['finishtime'].widget.attrs = {'class': 'form-control form_datetime', 'readonly': 'True'}
        self.fields['reason'].label = u'超时理由'
        self.fields['reason'].widget.attrs = {'class': 'form-control'}
        self.fields['batch'].label = u'项目批次'
        self.fields['batch'].widget.attrs = {'class': 'form-control'}
        self.fields['batch'].widget.choices = BATCH_CHOICES
        self.fields['remark'].label = u'备注'
        self.fields['remark'].widget.attrs = {'class': 'form-control'}

'''
class ProjectQueryForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('env', 'shortname', 'projectname', 'createuser', 'batch')
        widgets = {
            'env': forms.Select(),
            'shortname': forms.TextInput(),
            'projectname': forms.TextInput(),
            'createuser': forms.Select(),
            'batch': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectQueryForm, self).__init__(*args, **kwargs)
        self.fields['env'].label = u'环境'
        self.fields['env'].widget.choices = ENV_CHOICES
        self.fields['env'].widget.attrs = {'class': 'form-control', 'placeholder': '请选择项目环境'}
        self.fields['shortname'].label = u'简称'
        self.fields['shortname'].widget.attrs = {'class': 'form-control', 'placeholder': '项目简称'}
        self.fields['projectname'].label = u'名称'
        self.fields['projectname'].widget.attrs = {'class': 'form-control', 'placeholder': '项目名称'}
        self.fields['createuser'].label = u'搭建人员'
        self.fields['createuser'].widget.attrs = {'class': 'form-control', 'placeholder': '搭建人员'}
        self.fields['batch'].label = u'批次'
        self.fields['batch'].widget.attrs = {'class': 'form-control', 'placeholder': '项目批次'}
        self.fields['batch'].widget.choices = BATCH_CHOICES
'''


class VmForm(forms.ModelForm):
    class Meta:
        model = Vm
        fields = ('vmname', 'project', 'pm', 'role', 'cluster', 'os', 'soft', 'cpu', 'mem', 'disk', 'ip', 'vip', 'scan',
                  'mask', 'gateway', 'domain', 'admin', 'appuser')
        widgets = {
            'vmname': forms.TextInput(),
            'project': forms.Select(),
            'pm': forms.Select(),
            'role': forms.Select(),
            'cluster': forms.Select(),
            'os': forms.Select(),
            'soft': forms.Select(),
            'cpu': forms.TextInput(),
            'mem': forms.TextInput(),
            'disk': forms.TextInput(),
            'ip': forms.TextInput(),
            'vip': forms.TextInput(),
            'scan': forms.TextInput(),
            'mask': forms.Select(),
            'gateway': forms.TextInput(),
            'domain': forms.Select(),
            'admin': forms.TextInput(),
            'appuser': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VmForm, self).__init__(*args, **kwargs)
        self.fields['vmname'].label = u'服务器名称'
        self.fields['vmname'].error_messages = {'required': u'请输入服务器名称'}
        self.fields['vmname'].widget.attrs = {'class': 'form-control'}
        self.fields['project'].label = u'所属项目'
        self.fields['project'].widget.attrs = {'class': 'form-control'}
        self.fields['pm'].label = u'所属物理机'
        self.fields['pm'].widget.attrs = {'class': 'form-control', 'onchange': 'javascript:vm();return false;'}
        self.fields['role'].label = u'服务器功能'
        self.fields['role'].widget.attrs = {'class': 'form-control'}
        self.fields['role'].widget.choices = VMROLE_CHOICES
        self.fields['cluster'].label = u'集群'
        self.fields['cluster'].widget.attrs = {'class': 'form-control', 'onchange': 'javascript:vm();return false;'}
        self.fields['os'].label = u'操作系统'
        self.fields['os'].error_messages = {'required': u'请选择操作系统'}
        self.fields['os'].widget.attrs = {'class': 'form-control'}
        self.fields['os'].widget.choices = OS_CHOICES
        self.fields['soft'].label = u'安装软件'
        self.fields['soft'].widget.attrs = {'class': 'form-control'}
        self.fields['cpu'].label = u'CPU核数'
        self.fields['cpu'].error_messages = {'invalid': u'请输入数字'}
        self.fields['cpu'].widget.attrs = {'class': 'form-control'}
        self.fields['mem'].label = u'内存大小'
        self.fields['mem'].widget.attrs = {'class': 'form-control'}
        self.fields['mem'].error_messages = {'invalid': u'请输入数字'}
        self.fields['disk'].label = u'磁盘大小'
        self.fields['disk'].widget.attrs = {'class': 'form-control'}
        self.fields['disk'].error_messages = {'invalid': u'请输入数字'}
        self.fields['ip'].label = u'IP地址'
        self.fields['ip'].error_messages = {'required': u'请输入IP地址', 'invalid': u'请输入正确的IP地址'}
        self.fields['ip'].widget.attrs = {'class': 'form-control'}
        self.fields['vip'].label = u'VIP地址'
        self.fields['vip'].error_messages = {'required': u'请输入VIP地址', 'invalid': u'请输入正确的VIP地址'}
        self.fields['vip'].widget.attrs = {'class': 'form-control'}
        self.fields['scan'].label = u'SCANIP地址'
        self.fields['scan'].error_messages = {'required': u'请输入SCANIP地址', 'invalid': u'请输入正确的SCANIP地址'}
        self.fields['scan'].widget.attrs = {'class': 'form-control'}
        self.fields['mask'].label = u'子网掩码'
        self.fields['mask'].widget.choices = MASK_CHOICES
        self.fields['mask'].widget.attrs = {'class': 'form-control'}
        self.fields['gateway'].label = u'网关'
        self.fields['gateway'].widget.attrs = {'class': 'form-control'}
        self.fields['domain'].label = u'所在域'
        self.fields['domain'].widget.attrs = {'class': 'form-control'}
        self.fields['admin'].label = u'管理员'
        self.fields['admin'].widget.attrs = {'class': 'form-control'}
        self.fields['appuser'].label = u'应用用户'
        self.fields['appuser'].widget.attrs = {'class': 'form-control'}

'''
class VmQueryForm(forms.ModelForm):
    class Meta:
        model = Vm
        fields = ('vmname', 'project', 'role', 'os', 'ip')
        widgets = {
            'vmname': forms.TextInput(),
            'project': forms.Select(),
            'role': forms.Select(),
            'os': forms.Select(),
            'ip': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VmQueryForm, self).__init__(*args, **kwargs)
        self.fields['vmname'].label = u'名称'
        self.fields['vmname'].widget.attrs = {'class': 'form-control', 'placeholder': '虚拟机名称'}
        self.fields['project'].label = u'所属项目'
        self.fields['project'].widget.attrs = {'class': 'form-control', 'placeholder': '所属项目'}
        self.fields['role'].label = u'功能'
        self.fields['role'].widget.attrs = {'class': 'form-control', 'placeholder': '功能' }
        self.fields['role'].widget.choices = VMROLE_CHOICES
        self.fields['os'].label = u'系统'
        self.fields['os'].widget.attrs = {'class': 'form-control', 'placeholder': '操作系统'}
        self.fields['os'].widget.choices = OS_CHOICES
        self.fields['ip'].label = u'IP'
        self.fields['ip'].widget.attrs = {'class': 'form-control', 'placeholder': '虚拟机IP'}
'''


class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ('clustername', 'platform', 'vcaddress', 'vlangroup', 'storagegroup', 'remark')
        widgets = {
            'clustername': forms.TextInput(),
            'platform': forms.Select(),
            'vcaddress': forms.Select(),
            'vlangroup': forms.Select(),
            'storagegroup': forms.Select(),
            'remark': forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super(ClusterForm, self).__init__(*args, **kwargs)
        self.fields['clustername'].label = u'集群名'
        self.fields['clustername'].error_messages = {'required': u'请输入集群名'}
        self.fields['clustername'].widget.attrs = {'class': 'form-control'}
        self.fields['platform'].label = u'平台'
        self.fields['platform'].error_messages = {'required': u'请选择平台'}
        self.fields['platform'].widget.attrs = {'class': 'form-control'}
        self.fields['platform'].widget.choices = PLATFORM_CHOICES
        self.fields['vcaddress'].label = u'vc地址'
        self.fields['vcaddress'].error_messages = {'required': u'请选择vc地址'}
        self.fields['vcaddress'].widget.attrs = {'class': 'form-control'}
        self.fields['vcaddress'].widget.choices = VC_IP_CHOICES
        self.fields['vlangroup'].label = u'集群所属网络组'
        self.fields['vlangroup'].widget.attrs = {'class': 'form-control'}
        self.fields['vlangroup'].error_messages = {'required': u'请选择集群网段组', 'invalid': u'此网络组已被选择'}
        self.fields['storagegroup'].label = u'集群所属存储组'
        self.fields['storagegroup'].widget.attrs = {'class': 'form-control'}
        self.fields['storagegroup'].error_messages = {'required': u'请选择集群存储组', 'invalid': u'此存储组已被选择'}
        self.fields['remark'].label = u'备注'
        self.fields['remark'].widget.attrs = {'class': 'form-control'}


class PmForm(forms.ModelForm):
    class Meta:
        model = Pm
        fields = ('role', 'pmname', 'sn', 'cluster', 'project', 'vlangroup', 'storagegroup', 'pmtype', 'cpu',
                  'memory', 'disk', 'os', 'soft', 'eth', 'hba', 'hba_wwn', 'ip', 'ilo_ip', 'mask', 'gateway',
                  'domain', 'jiguihao', 'jiguiwei', 'position', 'remark')
        widgets = {
            'role': forms.Select(),
            'pmname': forms.TextInput(),
            'ip': forms.TextInput(),
            'ilo_ip': forms.TextInput(),
            'sn': forms.TextInput(),
            'cluster': forms.Select(),
            'project': forms.Select(),
            'vlangroup': forms.Select(),
            'storagegroup': forms.Select(),
            'pmtype': forms.TextInput(),
            'cpu': forms.TextInput(),
            'memory': forms.TextInput(),
            'disk': forms.TextInput(),
            'os': forms.Select(),
            'soft': forms.Select(),
            'eth': forms.TextInput(),
            'hba': forms.TextInput(),
            'hba_wwn': forms.TextInput(),
            'mask': forms.Select(),
            'gateway': forms.TextInput(),
            'domain': forms.Select(),
            'jiguihao': forms.TextInput(),
            'jiguiwei': forms.TextInput(),
            'position': forms.Select(),
            'remark': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(PmForm, self).__init__(*args, **kwargs)
        self.fields['pmname'].label = u'主机名'
        self.fields['sn'].label = u'序列号'
        self.fields['cluster'].label = u'所属集群'
        self.fields['project'].label = u'所属项目'
        self.fields['vlangroup'].label = u'所属网段组'
        self.fields['storagegroup'].label = u'所属存储组'
        self.fields['cpu'].label = u'CPU核数'
        self.fields['memory'].label = u'内存'
        self.fields['os'].label = u'操作系统'
        self.fields['soft'].label = u'安装软件'
        self.fields['ip'].label = u'IP地址'
        self.fields['ilo_ip'].label = u'管理地址'
        self.fields['eth'].label = u'网卡数'
        self.fields['hba'].label = u'HBA卡'
        self.fields['jiguihao'].label = u'机柜号'
        self.fields['jiguiwei'].label = u'机柜位'
        self.fields['pmtype'].label = u'设备类型'
        self.fields['role'].label = u'功能'
        self.fields['disk'].label = u'磁盘'
        self.fields['hba_wwn'].label = u'HBAWWN'
        self.fields['domain'].label = u'所属域'
        self.fields['mask'].label = u'子网掩码'
        self.fields['gateway'].label = u'网关'
        self.fields['position'].label = u'机房'
        self.fields['remark'].label = u'备注'
        
        self.fields['pmname'].error_messages = {'required': u'请输入主机名'}
        self.fields['ip'].error_messages = {'required': u'请输入IP地址', 'invalid': u'请输入正确的IP地址'}
        self.fields['ilo_ip'].error_messages = {'required': u'请输入管理IP地址', 'invalid': u'请输入正确的IP地址'}
        self.fields['gateway'].error_messages = {'invalid': u'请输入正确的IP地址'}
        self.fields['cpu'].error_messages = {'invalid': u'请输入数字'}
        self.fields['memory'].error_messages = {'invalid': u'请输入数字'}
        self.fields['eth'].error_messages = {'invalid': u'请输入数字'}
        self.fields['hba'].error_messages = {'invalid': u'请输入数字'}
        self.fields['disk'].error_messages = {'invalid': u'请输入数字'}
        
        self.fields['pmname'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['sn'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['cluster'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['project'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['vlangroup'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['storagegroup'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['cpu'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['memory'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['os'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['soft'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['ip'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['ilo_ip'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['eth'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['hba'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['jiguihao'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['jiguiwei'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['pmtype'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['role'].widget.attrs = {'class': 'form-control', 'onchange': 'javascript:listchange();'
                                            'return false;', 'style': 'display:block'}
        self.fields['disk'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['hba_wwn'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['domain'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['mask'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['gateway'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['position'].widget.attrs = {'class': 'form-control', 'style': 'display:block'}
        self.fields['remark'].widget.attrs = {'class': 'form-control', 'cols': 120, 'rows': 2, 'style': 'display:block'}

        self.fields['os'].widget.choices = OS_CHOICES
        self.fields['mask'].widget.choices = MASK_CHOICES
        self.fields['position'].widget.choices = POSITION_CHOICES
        self.fields['role'].widget.choices = ROLE_CHOICES

'''
class PmQueryForm(forms.ModelForm):
    class Meta:
        model = Pm
        fields = ('role', 'pmname', 'pmtype', 'os', 'ip')
        widgets = {
            'role': forms.Select(),
            'pmname': forms.TextInput(),
            'ip': forms.TextInput(),
            'pmtype': forms.TextInput(),
            'os': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(PmQueryForm, self).__init__(*args, **kwargs)
        self.fields['pmname'].label = u'主机名'
        self.fields['os'].label = u'系统'
        self.fields['ip'].label = u'IP'
        self.fields['pmtype'].label = u'设备类型'
        self.fields['role'].label = u'功能'
        self.fields['pmname'].widget.attrs = {'class': 'form-control', 'placeholder': '物理机名称'}
        self.fields['os'].widget.attrs = {'class': 'form-control', 'placeholder': '操作系统'}
        self.fields['ip'].widget.attrs = {'class': 'form-control', 'placeholder': 'IP地址'}
        self.fields['pmtype'].widget.attrs = {'class': 'form-control', 'placeholder': '物理机类型'}
        self.fields['role'].widget.attrs = {'class': 'form-control', 'placeholder': '服务器功能'}
        self.fields['os'].widget.choices = OS_CHOICES
        self.fields['role'].widget.choices = ROLE_CHOICES
'''
