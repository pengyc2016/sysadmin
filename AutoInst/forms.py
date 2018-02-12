# coding=utf-8
from django import forms


class JbossForm(forms.Form):
    jbosslist = forms.CharField(label=u'JBOSS地址', error_messages={'required': u'请输入Jboss服务器IP地址'},
                                widget=forms.Textarea(attrs={'rows': 2, 'id': 'id_jbosslist', 'class': 'form-control'}),
                                required=True)
    apachelist = forms.CharField(label=u'APACHE地址',
                                 widget=forms.Textarea(attrs={'rows': 2, 'id': 'id_apachelist',
                                                              'class': 'form-control'}), required=False)
    jbossversion = forms.CharField(label=u'版本', error_messages={'required': u'请选择JBOSS版本'},
                                   widget=forms.Select(attrs={'id': 'id_jbossversion', 'class': 'form-control'},
                                                       choices=((6.4, u'6.4'), (6.1, u'6.1'))))
    sysname = forms.CharField(label=u'系统简称',
                              error_messages={'required': u'请输入系统简称'},
                              widget=forms.TextInput(attrs={'id': 'id_sysname', 'class': 'form-control'}))
    password = forms.CharField(label=u'管理员密码', error_messages={'required': u'请选择root密码'},
                               widget=forms.TextInput(attrs={'id': 'id_password', 'class': 'form-control'}))


class ApacheForm(forms.Form):
    apachelist = forms.CharField(label=u'APACHE地址', error_messages={'required': u'请输入Apache服务器IP地址'},
                                 widget=forms.Textarea(attrs={'rows': 2, 'id': 'id_apachelist',
                                                              'class': 'form-control'}), required=True)
    password = forms.CharField(label=u'管理员密码', error_messages={'required': u'请选择root密码'},
                               widget=forms.TextInput(attrs={'id': 'id_password', 'class': 'form-control'}))


class ZookeeperForm(forms.Form):
    zookeeperlist = forms.CharField(label=u'Zookeeper地址', error_messages={'required': u'请输入zookeeper服务器IP地址'},
                                    widget=forms.Textarea(attrs={'rows': 3, 'id': 'id_zookeeperlist',
                                                                 'class': 'form-control'}), required=True)
    zookeeperversion = forms.CharField(label=u'版本', error_messages={'required': u'请选择zookeeper版本'},
                                       widget=forms.Select(attrs={'id': 'id_zookeeperversion', 'class': 'form-control'},
                                                           choices=(('3.4.5', u'3.4.5'), ('3.4.6', u'3.4.6'))))
    password = forms.CharField(label=u'管理员密码', error_messages={'required': u'请选择root密码'},
                               widget=forms.TextInput(attrs={'id': 'id_password', 'class': 'form-control'}))


class MongoForm(forms.Form):
    master = forms.CharField(label=u'主地址', error_messages={'required': u'请输入mongo主服务器IP地址'},
                             widget=forms.TextInput(attrs={'id': 'id_master', 'class': 'form-control'}), required=True)
    slave = forms.CharField(label=u'从地址', widget=forms.TextInput(attrs={'id': 'id_slave', 'class': 'form-control'}))
    mongoversion = forms.CharField(label=u'版本', error_messages={'required': u'请选择mongo版本'},
                                   widget=forms.Select(attrs={'id': 'id_mongoversion', 'class': 'form-control'},
                                                       choices=(('3.2.3', u'3.2.3'), ('2.6.3', u'2.6.3'),
                                                                ('2.4.5', u'2.4.5'))))
    password = forms.CharField(label=u'管理员密码', error_messages={'required': u'请选择root密码'},
                               widget=forms.TextInput(attrs={'id': 'id_password', 'class': 'form-control'}))


class MongoreplsetForm(forms.Form):
    mongolist = forms.CharField(label=u'MongoDB地址', error_messages={'required': u'请输入mongo服务器IP地址'},
                                widget=forms.Textarea(attrs={'rows': 2, 'id': 'id_mongolist', 'class': 'form-control'}),
                                required=True)
    arbiter = forms.CharField(label=u'MongoDB仲裁地址',
                              widget=forms.TextInput(attrs={'id': 'id_arbiter', 'class': 'form-control'}))
    mongoversion = forms.CharField(label=u'版本', error_messages={'required': u'请选择mongo版本'},
                                   widget=forms.Select(attrs={'id': 'id_mongoversion', 'class': 'form-control'},
                                                       choices=(('3.2.3', u'3.2.3'), ('2.6.3', u'2.6.3'),
                                                                ('2.4.5', u'2.4.5'))))
    password = forms.CharField(label=u'管理员密码', error_messages={'required': u'请选择root密码'},
                               widget=forms.TextInput(attrs={'id': 'id_password', 'class': 'form-control'}))
