from django.conf.urls import patterns, url

urlpatterns = patterns('UserManage.views',
    url(r'^login/$', 'user.loginuser', name='loginurl'),
    url(r'^logout/$', 'user.logoutuser', name='logouturl'),

    url(r'^user/add/$', 'user.adduser', name='adduserurl'),
    url(r'^user/list/$', 'user.listuser', name='listuserurl'),
    url(r'^user/edit/(?P<num>\d+)/$', 'user.edituser', name='edituserurl'),
    url(r'^user/delete/(?P<num>\d+)/$', 'user.deleteuser', name='deleteuserurl'),
    url(r'^user/showproject/(?P<num>\d+)/$', 'user.showproject', name='showproject'),
    url(r'^user/showvm/(?P<num>\d+)/$', 'user.showvm', name='showvm'),

    url(r'^user/changepwd/$', 'user.changepassword', name='changepasswordurl'),
    url(r'^user/resetpwd/(?P<num>\d+)/$', 'user.resetpassword', name='resetpasswordurl'),

    url(r'^role/add/$', 'role.addrole', name='addroleurl'),
    url(r'^role/list/$', 'role.listrole', name='listroleurl'),
    url(r'^role/edit/(?P<num>\d+)/$', 'role.editrole', name='editroleurl'),
    url(r'^role/delete/(?P<num>\d+)/$', 'role.deleterole', name='deleteroleurl'),

    url(r'^permission/deny/$', 'permission.nopermission', name='permissiondenyurl'),

    url(r'^permission/add/$', 'permission.addpermission', name='addpermissionurl'),
    url(r'^permission/list/$', 'permission.listpermission', name='listpermissionurl'),
    url(r'^permission/edit/(?P<num>\d+)/$', 'permission.editpermission', name='editpermissionurl'),
    url(r'^permission/delete/(?P<num>\d+)/$', 'permission.deletepermission', name='deletepermissionurl'),
)
