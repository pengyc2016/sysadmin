#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from ResourceManage.models import Vlan,VlanGroup,Software,Domain,Storage,StorageGroup
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

# RAID选项
RAIDTYPE_CHOICES = (('', '---------'),
                    ('RAID0', 'RAID0'),
                    ('RAID1', 'RAID1'),
                    ('RAID1+0', 'RAID1+0'),
                    ('RAID5', 'RAID5'),
                    ('NORAID', 'NORAID'),
                    )

# 软件类型选项
TYPE_CHOICES = (('', '---------'),
                ('中间件', '中间件'),
                ('开源中间件', '开源中间件'),
                #('操作系统', '操作系统'),
                ('数据库', '数据库'),
                ('其他', '其他')
                )

# 存储类型选项
STORAGETYPE_CHOICES = (('', '---------'),
                       ('HUAWEI', 'HUAWEI'),
                       ('EMC', 'EMC'),
                       ('HDS', 'HDS'),
                       ('其他', '其他')
                       )

# 掩码选项
MASK_CHOICES = (('', '---------'),
                ('255.255.255.0', '255.255.255.0'),
                ('255.255.255.128', '255.255.255.128'),
                ('255.255.0.0', '255.255.0.0')
                )


class VlanForm(forms.ModelForm):
    class Meta:
        model = Vlan
        fields = ('vlanname', 'startip', 'endip', 'gateway', 'mask', 'remark')
        widgets = {
            'vlanname': forms.TextInput(),
            'startip': forms.TextInput(),
            'endip': forms.TextInput(),
            'gateway': forms.TextInput(),
            'mask': forms.Select(),
            'remark': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VlanForm, self).__init__(*args, **kwargs)
        self.fields['vlanname'].label = u'网段名称'
        self.fields['vlanname'].widget.attrs = {'class': 'form-control'}
        self.fields['vlanname'].error_messages = {'required': u'请输入网段名称', 'invalid': u'请输入正确网络地址段'}
        self.fields['startip'].label = u'起始IP'
        self.fields['startip'].error_messages = {'invalid': u'请输入数字'}
        self.fields['startip'].widget.attrs = {'class': 'form-control'}
        self.fields['endip'].label = u'结束IP'
        self.fields['endip'].widget.attrs = {'class': 'form-control'}
        self.fields['endip'].error_messages = {'invalid': u'请输入数字'}
        self.fields['gateway'].label = u'网关'
        self.fields['gateway'].widget.attrs = {'class': 'form-control'}
        self.fields['gateway'].error_messages = {'required': u'请输入网关', 'invalid': u'请输入网络地址段'}
        self.fields['mask'].label = u'子网掩码'
        self.fields['mask'].widget.attrs = {'class': 'form-control'}
        self.fields['mask'].widget.choices = MASK_CHOICES
        self.fields['mask'].error_messages = {'required': u'请选择子网掩码', 'invalid': u'请输入网络地址段'}
        self.fields['remark'].label = u'备注'
        self.fields['remark'].widget.attrs = {'class': 'form-control'}


class VlanGroupForm(forms.ModelForm):
    class Meta:
        model = VlanGroup
        fields = ('vlangroupname', 'vlan', 'remark')
        widgets = {
            'vlangroupname': forms.TextInput(attrs={'class': 'form-control'}),
            'vlan': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10', 'multiple': 'multiple'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(VlanGroupForm, self).__init__(*args, **kwargs)
        self.fields['vlangroupname'].label = u'网段组名称'
        self.fields['vlangroupname'].error_messages = {'required': u'请输入网段组名称'}
        self.fields['vlan'].label = u'网段名称'
        self.fields['vlan'].required = False
        self.fields['remark'].label = u'备注'


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('softwarename', 'version', 'platform', 'arch', 'doc', 'path', 'softtype', 'remark')
        widgets = {
            'softwarename': forms.TextInput(),
            'version': forms.TextInput(),
            'platform': forms.Select(),
            'arch': forms.Select(),
            'doc': forms.TextInput(),
            'path': forms.TextInput(),
            'softtype': forms.Select(),
            'remark': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(SoftwareForm, self).__init__(*args, **kwargs)
        self.fields['softwarename'].label = u'软件名称'
        self.fields['version'].label = u'软件版本'
        self.fields['platform'].label = u'所属平台'
        self.fields['arch'].label = u'软件架构'
        self.fields['doc'].label = u'文档'
        self.fields['path'].label = u'软件路径'
        self.fields['softtype'].label = u'软件类型'
        self.fields['remark'].label = u'备注'

        self.fields['softwarename'].error_messages = {'required': u'请输入软件名称'}
        self.fields['version'].error_messages = {'required': u'请输入软件版本'}
        self.fields['platform'].error_messages = {'required': u'请选择软件平台'}
        self.fields['arch'].error_messages = {'required': u'请选择软件架构'}
        self.fields['softtype'].error_messages = {'required': u'请选择软件类型'}
        self.fields['softwarename'].widget.attrs = {'class': 'form-control'}
        self.fields['version'].widget.attrs = {'class': 'form-control'}
        self.fields['platform'].widget.attrs = {'class': ' form-control'}
        self.fields['arch'].widget.attrs = {'class': 'form-control'}
        self.fields['doc'].widget.attrs = {'class': 'form-control'}
        self.fields['path'].widget.attrs = {'class': 'form-control'}
        self.fields['softtype'].widget.attrs = {'class': 'form-control'}
        self.fields['remark'].widget.attrs = {'class': 'form-control', 'cols': 120, 'rows': 2}

        self.fields['arch'].widget.choices = ARCH_CHOICES
        self.fields['softtype'].widget.choices = TYPE_CHOICES
        self.fields['platform'].widget.choices = PLATFORM_CHOICES


class StorageGroupForm(forms.ModelForm):
    class Meta:
        model = StorageGroup
        fields = ('storagegroupname', 'remark')
        widgets = {
            'storagegroupname': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StorageGroupForm, self).__init__(*args, **kwargs)
        self.fields['storagegroupname'].label = u'存储组名称'
        self.fields['storagegroupname'].error_messages = {'required': u'请输入存储组名称'}
        self.fields['remark'].label = u'备注'
        self.fields['remark'].widget.attrs = {'class': 'form-control'}


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('storagename', 'storagesize', 'storagetype', 'raidtype', 'storagegroup', 'remark')
        widgets = {
            'storagename': forms.TextInput(),
            'storagesize': forms.TextInput(),
            'storagetype': forms.Select(),
            'raidtype': forms.Select(),
            'storagegroup': forms.Select(),
            'remark': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(StorageForm, self).__init__(*args, **kwargs)
        self.fields['storagename'].label = u'存储名称'
        self.fields['storagename'].widget.attrs = {'class': 'form-control'}
        self.fields['storagename'].error_messages = {'required': u'请输入存储名称'}
        self.fields['storagesize'].label = u'存储大小(G)'
        self.fields['storagesize'].widget.attrs = {'class': 'form-control'}
        self.fields['storagesize'].error_messages = {'required': u'请输入存储大小', 'invalid': u'请输入数字，单位为G'}
        self.fields['storagetype'].label = u'存储类型'
        self.fields['storagetype'].widget.attrs = {'class': 'form-control'}
        self.fields['storagetype'].error_messages = {'required': u'请输入存储类型'}
        self.fields['storagetype'].widget.choices = STORAGETYPE_CHOICES
        self.fields['raidtype'].label = u'RAID类型'
        self.fields['raidtype'].widget.attrs = {'class': 'form-control'}
        self.fields['raidtype'].error_messages = {'required': u'请输入RAID类型'}
        self.fields['raidtype'].widget.choices = RAIDTYPE_CHOICES
        self.fields['storagegroup'].label = u'所属存储组'
        self.fields['storagegroup'].widget.attrs = {'class': 'form-control'}
        self.fields['storagegroup'].error_messages = {'required': u'请选择存储组'}
        self.fields['remark'].label = u'备注'
        self.fields['remark'].widget.attrs = {'class': 'form-control'}


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ('domainname', 'DNS', 'remark')
        widgets = {
            'domainname': forms.TextInput(attrs={'class': 'form-control'}),
            'DNS': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DomainForm, self).__init__(*args, **kwargs)
        self.fields['domainname'].label = u'域名称'
        self.fields['domainname'].error_messages = {'required': u'请输入域名称'}
        self.fields['DNS'].label = u'DNS名称'
        self.fields['DNS'].error_messages = {'required': u'请输入DNS名称', 'invalid': u'请输入网络地址段'}
        self.fields['remark'].widget.attrs = {'class': 'form-control'}
        self.fields['remark'].label = u'备注'


