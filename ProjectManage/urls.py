from django.conf.urls import patterns, url

urlpatterns = patterns('ProjectManage.views',
    url(r'^project/list/$', 'project.project_list', name='projectlist'),
    url(r'^project/input/$', 'project.project_input', name='projectinput'),
    url(r'^project/query/$', 'project.project_query', name='projectquery'),
    url(r'^project/export/$', 'project.project_export', name='projectexport'),
    url(r'^project/edit/(?P<num>\d+)/$', 'project.project_edit', name='projectedit'),
    url(r'^project/delete/(?P<num>\d+)/$', 'project.project_delete', name='projectdelete'),
    url(r'^project/showvm/(?P<num>\d+)/$', 'project.project_show_vm', name='projectshowvm'),
    url(r'^vm/list/$', 'vm.vm_list', name='vmlist'),
    url(r'^vm/input/$', 'vm.vm_input', name='vminput'),
    url(r'^vm/query/$', 'vm.vm_query', name='vmquery'),
    url(r'^vm/edit/(?P<num>\d+)/$', 'vm.vm_edit', name='vmedit'),
    url(r'^vm/repl/(?P<num>\d+)/$', 'vm.vm_replication', name='vmrepl'),
    url(r'^vm/delete/(?P<num>\d+)/$', 'vm.vm_delete', name='vmdelete'),
    url(r'^vm/export/$', 'vm.vm_export', name='vmexport'),
    url(r'^vm/getip/$', 'getip.get_ip', name='getip'),
    url(r'^vm/update/(?P<num>\d+)$', 'vm.vm_update', name='vmupdate'),
    url(r'^cluster/list/$', 'cluster.cluster_list', name='clusterlist'),
    url(r'^cluster/input/$', 'cluster.cluster_input', name='clusterinput'),
    url(r'^cluster/query/$', 'cluster.cluster_query', name='clusterquery'),
    url(r'^cluster/export/$', 'cluster.cluster_export', name='clusterexport'),
    url(r'^cluster/edit/(?P<num>\d+)/$', 'cluster.cluster_edit', name='clusteredit'),
    url(r'^cluster/flush/$', 'cluster.cluster_flush', name='clusterflush'),
    url(r'^cluster/delete/(?P<num>\d+)/$', 'cluster.cluster_delete', name='clusterdelete'),
    url(r'^cluster/showpm/(?P<num>\d+)/$', 'cluster.cluster_show_pm', name='clustershowpm'),
    url(r'^cluster/showvm/(?P<num>\d+)/$', 'cluster.cluster_show_vm', name='clustershowvm'),
    url(r'^pm/list/$', 'pm.pm_list', name='pmlist'),
    url(r'^pm/input/$', 'pm.pm_input', name='pminput'),
    url(r'^pm/query/$', 'pm.pm_query', name='pmquery'),
    url(r'^pm/export/$', 'pm.pm_export', name='pmexport'),
    url(r'^pm/edit/(?P<num>\d+)/$', 'pm.pm_edit', name='pmedit'),
    url(r'^pm/delete/(?P<num>\d+)/$', 'pm.pm_delete', name='pmdelete'),
    url(r'^pm/repl/(?P<num>\d+)/$', 'pm.pm_replication', name='pmrepl'),
)