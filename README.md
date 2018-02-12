#sysadmin系统管理平台

###版本：
    python v2.7
    django v1.8
    Bootstrap v3.2.0
	
###部署：
	1.安装django 1.8，paramiko
	2.将项目解压在任意目录下，进入项目目录
	3.同步数据库，需要先创建好数据库，数据库连接信息在website/settings.py文件中定义
		# python manage.py makemigration
                # python manage.py migrate
	4.运行项目
		# python manage.py runserver 0.0.0.0:80
	5.浏览器访问
	
###权限判断逻辑：
	1.用户隶属于某个角色（组的概念），角色具有一定的权限
	2.当用户访问某个url时，获取当用户的用户名和要访问的URL地址，判断用户隶属的角色是否包含所以访问的url

###内容:
        1、用户管理
        2、项目管理
        3、集群管理
        4、虚拟机管理
        5、物理机管理
        6、地址管理
        7、存储管理

###Git:
<li>GitHub:<https://github.com/pengyc2016/sysadmin></li>
<li>GitOsc:<https://git.oschina.net/pengyc/sysadmin></li>


