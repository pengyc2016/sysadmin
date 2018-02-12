from django.conf.urls import patterns, url

urlpatterns = patterns('AutoInst.views',
    url(r'^jboss/$', 'jboss.jboss', name='jboss'),
    url(r'^jbosshelp/$', 'jboss.jbosshelp', name='jbosshelp'),
    url(r'^apache/$', 'apache.apache', name='apache'),
    url(r'^apachehelp/$', 'apache.apachehelp', name='apachehelp'),
    url(r'^zookeeper/$', 'zookeeper.zookeeper', name='zookeeper'),
    url(r'^zookeeperhelp/$', 'zookeeper.zookeeperhelp', name='zookeeperhelp'),
    url(r'^mongo/$', 'mongo.mongo', name='mongo'),
    url(r'^mongoreplset/$', 'mongo.mongoreplset', name='mongoreplset'),
    url(r'^mongohelp/$', 'mongo.mongohelp', name='mongohelp'),
)
